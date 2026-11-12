# What's New

The version of the app you have (its build date and code version) is shown at Settings › **Diagnostics**.

## 2026-11-12

- **Listen like other audio:** listening goes on with the screen locked or in another app, also with a device voice, and the app shows on the lock screen and in Control Center with the proposal's title, the page, and the time left. Play, pause, next and previous sentence, and dragging the progress bar work from there and from AirPods. Taking out your AirPods, a call, or audio from another app pauses the reading.
- **Review types:** NSF, NASA, JWST, general observing, and general funding. Each sets the criteria strengths and weaknesses are filed under, the rating (E to P with split ratings for NSF and NASA; three averaged grades for JWST), the review's fields, and the layout of the notes report and the copied text. The type is guessed from the proposal, and highlights are filed by the section they are in. See [Review Types](docs/review-types.md).
- **Natural voice on iPhone:** the voice engine restarts between sentences every 90 seconds of work or 8 sentences, to free memory before Safari closes the page.
- **Preparing ahead while listening on a device voice** is now tested and documented.
- **Help** in Settings links to this guide and to the privacy details, and Settings › Diagnostics shows the version.
- **Voice tips:** the iPhone tip no longer suggests downloading Enhanced or Premium voices, which Safari does not offer to web pages. There is now a tip for Windows.
- **This guide,** with screenshots.

## 2026-11-11

- **Natural voice stays on after a reload:** the Voice panel no longer asks to turn it on again, and the loading message says it loads from this device.
- **Restore state keeps device settings:** the voice worker limit and **Save state automatically** stay as each device has them. A device without the natural voice uses its own voice until you download it.
- **Preparing ahead continues** when you press play after Safari closed the page while preparing.
- **Memory logging** in the diagnostic log for the natural voice.
- **Sections list with dropdowns:** cover pages and the budget are folded into single entries, and sections fold their subsections.
- **Reading:** proposal titles, questions, and figure captions are read; cover pages are recognized; a second voice worker that does not fit in memory is not tried again.
- **Prepare ahead,** a silent track that keeps playback going while the voice catches up, and recovery after a crash of the natural voice.
- **Save state and Restore state** in one file; reopen where you left off after a reload; automatic notes PDF.
- **The natural voice (Kokoro),** running on the device.
- **First version:** listen to proposal PDFs with the text following along, highlight and annotate, and export notes and annotated PDFs.
