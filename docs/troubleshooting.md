# Troubleshooting and FAQ

If something here does not help, see [Reporting a Problem](#reporting-a-problem) at the end.

## Voices and Sound

**I downloaded Premium or Enhanced voices on my iPhone, but they are not in the list.**
Safari offers web pages only the voices built into iOS; downloaded Enhanced and Premium voices are left out to reduce fingerprinting. No web app can use them. For a more natural voice, use **Voice and speed › Natural (on device)**.

**There is no sound.**
Check the volume, and that another app is not playing audio. If the natural voice is selected but shows an error, tap play to try again, or choose **Device voices** under **Voice and speed**.

**Reading stops when I lock the phone or switch apps.**
It should go on, like other audio (see [The Lock Screen, Other Apps, and AirPods](iphone.md#the-lock-screen-other-apps-and-airpods)). Open the app from Safari, not from a Home Screen icon. If it still stops, keep the screen on (Settings › **Keep the screen on while playing**) and send the diagnostic log: it records when the screen went off and whether the page's audio was playing. In iOS 27, a Safari bug can stop device voices when the phone locks; the natural voice is not affected.

**The reading paused by itself.**
Taking out your headphones, a call, or audio from another app pauses the reading, as with other audio. Press play to continue.

**The natural voice keeps pausing ("Getting … of speech ready").**
On a phone, the natural voice is made more slowly than you listen. When it falls behind, it collects enough speech to then play for a while without stopping, and tells you how long that takes. For listening without waits, use **Prepare ahead** first (Voice and speed › **Prepare the rest of this proposal**), or listen at a lower speed.

**"The natural voice is not downloaded on this device yet."**
You chose the natural voice on another device, or restored a state from one, or the browser removed the voice's files. Play uses the device voice meanwhile. To use the natural voice here, choose **Voice and speed › Natural (on device) › Download and turn on** (about 104 MB, once).

**The Voice and speed panel closed by itself and the page reloaded.**
Safari reloads a page that used too much memory. The app reopens the proposal where you were, and the natural voice stays on: press play and it loads from this device. If this happened while preparing ahead, preparing continues when you press play. See [Memory, and When Safari Reloads the Page](iphone.md#memory-and-when-safari-reloads-the-page). If it keeps happening, send the diagnostic log.

## Reading

**A table or figure is being read, or text I want is skipped.**
Settings › **Reading aloud** controls what is skipped: citations, the reference list, figure and table text, captions, footnotes, and web addresses. Skipped text is dimmed; tap a sentence to see whether it is skipped. If the app misjudges a part of a PDF, please report it. Describe the layout, but never share a confidential proposal.

**A word is mispronounced.**
Add it to Settings › **Pronunciations**, one per line, written as `text = how to say it`, for example `NOMIC = no mick`.

**"This PDF has no selectable text (it may be a scan), so it cannot be read aloud."**
The PDF contains images of pages rather than text. Ask for a text-based PDF, or run it through a text-recognition tool first.

**"This PDF is password-protected."**
Open it, save a copy without the password, and add that copy.

**An encrypted PDF opens, but the annotated export fails.**
Highlights cannot be written into an encrypted PDF. The notes report still works.

## Notes and Exports

**The review type is wrong.**
Open **Notes** and tap the right type under **Review**. Your highlights and notes stay as they are; only their grouping and labels change. See [Review Types](review-types.md).

**A strength is filed under the wrong criterion.**
Tap the highlight, choose **Edit this … highlight**, and tap the right criterion.

**Where did my export go?**
Wherever your browser saves downloads. On iPhone: the Files app › Downloads, which is in iCloud Drive unless you choose **On My iPhone** under iOS Settings › Apps › Safari › Downloads.

**How do I paste my review into the review system?**
Notes › **Export notes** › **Copy review text** copies plain text laid out in the order of the program's form, with each section's heading in capitals. Paste section by section.

## Saving and Devices

**My proposals and notes are gone.**
The browser removed the app's data. Safari, for example, does this after 7 days of Safari use without visiting the site, and storage cleanups can too. Use **Restore state** with your newest **Proposal Listener State** file (on iPhone, usually in Files › Downloads), or add an annotated proposal PDF you exported. To be safe, use **Save state** now and then.

**How do I continue on another device?**
**Save state** on the first device, move the file (for example with AirDrop or Files), and **Restore state** on the other device. Or, for one proposal, export the **Annotated proposal (PDF)** and add it on the other device.

**Restoring merged my notes. Did I lose anything?**
No. Restoring keeps notes you made since the file was saved and adds the ones in the file; for a highlight in both, the newer one wins.

## Reporting a Problem

1. In the app, open **Settings › Copy diagnostic log**. The log has events, timings, and error messages, but no proposal text or file names.
2. Open an issue in [this repository](https://github.com/astrowagner/pdfreviewer/issues), describe what happened, and paste the log. Issues are public: never paste proposal text or attach a proposal.
