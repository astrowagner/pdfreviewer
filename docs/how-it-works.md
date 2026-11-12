# How It Works

For the technically curious. The whole app is `index.html` in this repository: one file with its code readable inside, plus the natural voice's files in `kokoro/`. It runs entirely in the browser.

## Reading a PDF

1. **Text extraction:** [PDF.js](https://github.com/mozilla/pdf.js) (6.2.108, legacy build) reads each page's text with positions and font sizes, in a worker, with time limits; if its worker stops responding, it tries once more on the main thread.
2. **Lines and page furniture:** text is joined into lines. Running headers, footers, and page numbers (lines repeated near the top or bottom of at least about a third of the pages) are set aside.
3. **Blocks:** lines are grouped into paragraphs, and paragraphs that continue across pages are joined.
4. **Classification:** each block is sorted as body text, heading, caption, footnote, figure or table text, or reference list, from its type size relative to the body text, rotation, how much of it is numbers, wide gaps between columns, and its neighbors. Rotated text and number-heavy blocks start a figure; short labels next to them (axis labels, legends, panel letters) join it. Form rows, questions, sentences, list items, and addresses are never figure text. Captions are recognized by their labels ("Figure 1:", "Table 2 –", and similar).
5. **Cover and form pages:** pages that read as forms (mostly labels, values, and tables) are detected, so the Sections list can fold the cover pages and the budget into single entries.
6. **Sentences and speech text:** blocks are split into sentences. For speech, citations, web addresses, and the reference list can be left out, abbreviations and units expanded (μm as "microns", β as "beta", 10⁻⁶ as "10 to the minus 6"), and your pronunciations applied.
7. **The review type** is guessed from the text of the first pages, running headers included (see [Review Types](review-types.md)).

When the parsing changes in a new version, stored proposals are read again the next time they are opened. Your place, the sentences you have heard, and your highlights are matched to the new text by the sentence text.

## Speaking

- **Device voices** use the browser's Web Speech API. Word boundaries from the voice move the highlight word by word.
- **The natural voice** is [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) v1.0 as an 8-bit ONNX model, run by [ONNX Runtime Web](https://github.com/microsoft/onnxruntime) 1.31.1 (WebAssembly, one thread) in a worker. Text is turned into phonemes by [espeak-ng](https://github.com/rhasspy/espeak-ng), compiled to WebAssembly, with English data only. The model speaks at the chosen speed, up to 2×. Long sentences are made in pieces of about 100 tokens (about 6 seconds), because working memory grows with the length of audio made at once. Word timings come from the phonemes and the pauses in the audio.
- **Files and checks:** the voice's files (about 104 MB) are this site's own files, checked by SHA-256 after download, and kept in the browser's storage. Data files are wrapped in minimal WebAssembly modules so any static host serves them.
- **Keeping ahead:** the voice makes speech up to 10 minutes ahead. When it falls behind, it collects enough speech to play for about 10 minutes, or to the end, without stopping, based on the measured pace. While waiting, a silent track keeps the page alive on iPhone with the screen locked. **Prepare ahead** stores the speech for the rest of a proposal in the browser's storage (up to 1 GB, oldest first out), so it plays later without loading the model.
- **Memory on iPhone:** in Chrome, one voice worker's WebAssembly memory grows from about 137 MB to 317 MB over the first sentences and then stays flat, and the whole renderer process stays flat (591–600 MB over 36 sentences). In Safari on an iPhone, the page was closed about 3 minutes into each run of the voice, and a restart of the voice reset that clock. So on iPhone the voice worker restarts between sentences after 90 seconds of work or 8 sentences, keeping its queue; it reloads from the device in about a second. A second worker is used only when one cannot keep up, and on iPhone only if you turn it on.
- **In the background:** Safari on iPhone keeps a hidden page running only while it plays audio. The natural voice plays its speech through one `<audio>` element. Device voices are spoken by the browser, not played by the page, so while one reads, the same element loops a silent 2-second WAV (all samples zero). The [Media Session API](https://developer.mozilla.org/en-US/docs/Web/API/Media_Session_API) gives the lock screen the title, page, artwork, and the position in the proposal (estimated from word counts at the learned speaking pace), and takes play, pause, stop, next and previous track (one sentence), and seek. When the element is paused from outside the app (headphones taken out, a call, another app's audio), the reading pauses. Safari in iOS 27 (reported in 27.0 to 27.2) pauses a page's audio when a device voice starts ([WebKit bug 218815](https://bugs.webkit.org/show_bug.cgi?id=218815)); a pause within 1.5 seconds of the first sentence's start is taken to be that, and the silent track is then left off until the page reloads.
- **Recovering:** a sentence that takes far too long restarts the voice; one that fails twice is skipped. If the voice crashes after it had been working, it restarts once and playback continues; a second failure soon after pauses with a message, rather than switching to a device voice that may be silent with the screen locked. If the page stops unexpectedly while preparing ahead, preparing continues when play is pressed, at most twice in a row.

## Storing and Moving

- **Storage:** IndexedDB holds the PDFs, the parsed text, notes and reviews, and settings; separate stores hold the voice's files and prepared speech. At startup the app asks the browser to keep its data (`navigator.storage.persist()`).
- **The state file** is a PDF whose cover page lists its contents. Its data are attachments: `proposal-listener-state.json` (notes, reviews, places, settings) and each proposal's original PDF, each checked by size and SHA-256 on restore.
- **The annotated proposal** is the original PDF with highlight annotations (with appearance streams, so they display everywhere) and your notes as their comments. It also has `proposal-listener-notes.json` attached, so adding it to the app restores the highlights, notes, and review.
- **The notes report** is made with [pdf-lib](https://github.com/Hopding/pdf-lib), with DejaVu Sans subset at build time and embedded whole, so symbols and Greek letters print correctly.

## Security

The page's Content Security Policy:

```
default-src 'none'; script-src 'unsafe-inline' 'wasm-unsafe-eval'; style-src 'unsafe-inline';
img-src data: blob:; font-src data:; worker-src blob:; connect-src 'self' blob: data:;
media-src blob: data:; base-uri 'none'; form-action 'none'
```

It allows network requests only to the site itself, loads nothing from elsewhere, and submits no forms. See [Privacy and Data](privacy.md).

## Testing

The app is tested in headless Chrome at phone size, with simulated device speech and the real natural voice, using fictional test PDFs. The automated suites cover:

- what is read or skipped, and the Sections list;
- the main flows: adding PDFs, listening, highlighting, notes, exports, and page view;
- review types: guessing, filing by section, ratings and grades, export layouts, and the round trips below;
- the natural voice: download, playback, speed, recovery, Prepare ahead, and restarts;
- Save state and Restore state;
- automatic saving;
- a browser without newer stream features, as in older Safari (simulated in Chrome);
- the website served as on GitHub Pages.

The screenshots in this guide are made by a script from the same fictional PDFs.

## Components

See [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) for every included component, its version, and its license, and `LICENSES/` for the license texts.
