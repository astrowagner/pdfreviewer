# Third-Party Notices

Proposal Listener includes the components below. Full license texts are in `LICENSES/`.

| Component | Version | Used For | License | Source |
|---|---|---|---|---|
| PDF.js (legacy build) | 6.2.108 | Reading PDFs | Apache-2.0 | https://github.com/mozilla/pdf.js |
| pdf-lib | 1.17.1 | Writing the PDF exports | MIT | https://github.com/Hopding/pdf-lib |
| @pdf-lib/fontkit | 1.1.1 | Fonts in the PDF exports | MIT | https://github.com/Hopding/fontkit |
| DejaVu Sans (subsets) | as in Debian fonts-dejavu-core | Fonts in the PDF exports | Bitstream Vera license and public-domain changes | https://dejavu-fonts.github.io/ |
| ONNX Runtime Web | 1.31.1 | Running the voice model | MIT | https://github.com/microsoft/onnxruntime |
| Kokoro-82M v1.0, 8-bit ONNX (`model_quantized.onnx`, SHA-256 `fbae9257…1478`, obtained through the npm package kokoro-q8-shards 1.0.0) | 1.0 | The natural voice | Apache-2.0 | https://huggingface.co/hexgrad/Kokoro-82M, https://huggingface.co/onnx-community/Kokoro-82M-v1.0-ONNX |
| Kokoro voices | from kokoro-js 1.2.1 | Voice styles | Apache-2.0 | https://github.com/hexgrad/kokoro |
| Text normalization ported from kokoro-js | 1.2.1 | Reading numbers and symbols | Apache-2.0 | https://github.com/hexgrad/kokoro |
| espeak-ng (rhasspy fork) with piper-phonemize, compiled to WebAssembly by @diffusionstudio/piper-wasm 1.0.0; English data only | 1.0.0 | Phonemes for the natural voice | GPL-3.0-or-later (espeak-ng); MIT (piper-phonemize, piper-wasm) | https://github.com/rhasspy/espeak-ng, https://github.com/rhasspy/piper-phonemize, https://github.com/diffusion-studio/piper-wasm |
| Kokoro phoneme vocabulary (`config.json` from kokoro-onnx) | 0.6.1 | Tokens for the voice model | MIT | https://github.com/thewh1teagle/kokoro-onnx |

The phonemizer files are `kokoro/espeak-ng.wasm` and `kokoro/espeak-ng-en-data.wasm`. The English-only data were made from the data in @diffusionstudio/piper-wasm 1.0.0 with `tools/strip_espeak_data.py`; the build steps for the WebAssembly module are in the piper-wasm repository. The model is stored as a graph plus a weights file that hold the same tensors, split into parts. The data files in `kokoro/` (model parts, voices, phonemizer data) are wrapped in minimal WebAssembly modules, whose one custom section holds the bytes.
