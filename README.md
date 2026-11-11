# Proposal Listener

Listen to proposal PDFs like a podcast, mark strengths and weaknesses as you go, and export your review notes as PDF.

**Open the app:** https://astrowagner.github.io/pdfreviewer/

## Privacy

Everything runs in your browser. PDFs are read inside the page; the voice runs on your device (your device's own voices, or the natural voice after a one-time download of its files from this site); and your PDFs, highlights, notes, and place are stored in your browser on your device. Nothing is uploaded: the page may connect only to this site, to load its own files.

## Tips

- On iPhone, use it in Safari from a bookmark. Web apps added to the Home Screen often stop audio when the screen locks.
- Safari deletes a site's stored data after 7 days of Safari use without a visit to the site. Export your notes to keep them.
- Exported files go to Files › Downloads. Safari saves downloads to iCloud Drive unless you choose On My iPhone under Settings › Apps › Safari › Downloads.

## Contents

- `index.html`: the app, in one file (its code is readable in the file).
- `kokoro/`: the natural-voice files, downloaded on first use and checked by SHA-256.
- `THIRD_PARTY_NOTICES.md` and `LICENSES/`: the components the app includes, and their licenses.
- `tools/strip_espeak_data.py`: the script that made the English-only phonemizer data.
