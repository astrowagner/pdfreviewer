"""Build an English-only espeak-ng data package for the piper_phonemize WASM build.

Reads the Emscripten file-packager metadata from the glue JS, keeps only the files English
phonemization needs, writes a smaller .data file and a glue copy whose metadata points at it.

Usage: python3 -I strip_espeak_data.py <src_dir> <out_dir>
  src_dir: folder with piper_phonemize.js and piper_phonemize.data (from @diffusionstudio/piper-wasm 1.0.0)
  out_dir: folder to write piper_phonemize.js (patched) and espeak-en.data
"""
import hashlib
import json
import os
import sys

src_dir, out_dir = sys.argv[1], sys.argv[2]
glue = open(os.path.join(src_dir, 'piper_phonemize.js'), encoding='utf-8').read()
data = open(os.path.join(src_dir, 'piper_phonemize.data'), 'rb').read()

i = glue.index('loadPackage(') + len('loadPackage(')
meta, n = json.JSONDecoder().raw_decode(glue[i:])
assert meta['remote_package_size'] == len(data), 'data size does not match metadata'


def keep(name):
    parts = name.split('/')            # ['', 'espeak-ng-data', ...]
    if len(parts) == 3:                # top-level files: keep core tables and the English dictionary only
        base = parts[2]
        return base == 'en_dict' or not base.endswith('_dict')
    return parts[2] == 'lang'          # language definitions are tiny; voice variants and mbrola tables are not needed


out_files, chunks, pos = [], [], 0
for f in meta['files']:
    if not keep(f['filename']):
        continue
    blob = data[f['start']:f['end']]
    out_files.append({**f, 'start': pos, 'end': pos + len(blob)})
    chunks.append(blob)
    pos += len(blob)
new_data = b''.join(chunks)
new_meta = {**meta, 'files': out_files, 'remote_package_size': len(new_data)}
new_glue = glue[:i] + json.dumps(new_meta, separators=(',', ':')) + glue[i + n:]

os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, 'espeak-en.data'), 'wb') as fh:
    fh.write(new_data)
with open(os.path.join(out_dir, 'piper_phonemize.js'), 'w', encoding='utf-8') as fh:
    fh.write(new_glue)
kept = [f['filename'] for f in out_files]
print(f'kept {len(kept)} of {len(meta["files"])} files; data {len(data)} -> {len(new_data)} bytes')
print('top-level kept:', [k.split('/')[-1] for k in kept if k.count('/') == 2])
print('sha256 espeak-en.data', hashlib.sha256(new_data).hexdigest())
