# iPhone and iPad

Proposal Listener is made for Safari on iPhone and iPad. A few things work differently there.

## Open It in Safari, From a Bookmark

Use the app in Safari and bookmark https://astrowagner.github.io/pdfreviewer/. Avoid adding it to the Home Screen: web apps added to the Home Screen often stop audio when the screen locks, and they keep their own separate storage.

To add proposals, save the PDFs to the Files app (for example from Mail, or from your browser's downloads), then tap **Add proposal PDFs**.

## The Lock Screen, Other Apps, and AirPods

- **Listening goes on with the screen locked or in another app,** with either voice, and the app shows on the lock screen and in Control Center like other audio: the proposal's title, the page, and the time left. Safari keeps a page running in the background only while it plays audio. The natural voice is audio the page plays. A device voice is spoken by the system instead, so the app plays a silent track under it; otherwise Safari would stop after the sentence being spoken.
- **Controls:** play and pause from the lock screen, Control Center, or headphones. **Next** and **previous** go one sentence forward or back, and dragging the progress bar jumps to that point in the proposal. On AirPods with a stem control (AirPods Pro, and AirPods 3rd generation and later), press once to play or pause, twice for the next sentence, and three times for the previous one.
- **Taking out your AirPods, a call, or audio from another app pauses the reading,** as with other audio, so it does not go on through the phone's speaker.
- **If a device voice still stops when the phone locks,** keep the screen on (Settings › **Keep the screen on while playing**) and send the diagnostic log. Safari in iOS 27 (reported in 27.0 to 27.2) pauses a page's audio when a device voice starts speaking ([WebKit bug 218815](https://bugs.webkit.org/show_bug.cgi?id=218815), fixed in WebKit in November 2026). There, a device voice may stop when the phone locks; the natural voice is not affected.
- **Preparing ahead goes on in the background only while you listen.** If you switch apps or lock the phone while nothing is playing, Safari pauses the page, and preparing picks up when you return, unless Safari closed the page in the meantime; then start it again. The app keeps the screen on while preparing.

## Voices on iPhone

- **Device voices:** Safari offers web pages only the voices built into iOS. **Enhanced and Premium voices you download** in iOS Settings › Accessibility › Spoken Content **do not appear in the app**. Apple leaves them out to reduce fingerprinting, and no web app can use them. The natural voice is the way around this.
- **The natural voice** (Voice and speed › **Natural (on device)** › **Download and turn on**) downloads about 104 MB once. Use Wi-Fi.
- **It is made slower than real time on a phone:** about 1.3 seconds of work per second of speech on a recent iPhone. While you listen, it prepares ahead; when it falls behind, it collects enough speech to then play for a while without stopping, and says how long that takes.
- **For listening without waits, use Prepare ahead** before you start: Voice and speed › **Prepare the rest of this proposal**. Prepared speech is kept on the phone, plays without loading the voice model, also with the screen locked, and is there next time you open the proposal.
- **You can listen meanwhile.** Preparing goes on if you switch to **Device voices** and press play. On a phone, though, preparing will not catch up with where the device voice is reading, so this helps only for a later part of the proposal.

## Memory, and When Safari Reloads the Page

The natural voice uses about half a gigabyte of memory. Safari closes pages that use too much memory and then reloads them; the app is built to recover:

- **One voice worker on iPhone.** A second worker (Voice and speed › **Use two processor cores when needed**) is off by default on iPhone, because two need about 800 MB. If a second worker does not fit in memory, the app uses one from then on.
- **Regular restarts.** On iPhone the voice engine restarts itself between sentences every 90 seconds of work or 8 sentences, whichever comes first, to free its memory. It reloads from the phone in about a second, and nothing is lost. In diagnostic logs, Safari had closed the page about 3 minutes into each run of the voice, and a restart reset that clock.
- **After a reload,** the app reopens the proposal at the word where you stopped (Settings › **Reopen where I left off**). The natural voice stays on and loads from the phone when you press play; the message says it is loading from this device, not downloading.
- **If the page was closed while preparing ahead,** preparing continues the next time you press play in that proposal, and the app says so. After three closes in a row it stops continuing by itself, so a phone that cannot finish does not get stuck in a loop.

## Storage on iPhone

- **Safari can delete the app's data.** For example, it removes a site's stored data after 7 days of Safari use without a visit to the site. Use **Save state** now and then to keep everything in one file.
- **Where exported files go:** Files › Downloads, which is in iCloud Drive unless you choose **On My iPhone** under iOS Settings › Apps › Safari › Downloads. The state file and the annotated PDF contain the proposal, so choose where they go with care.
- **Inside claude.ai,** Safari erases the app's data when it quits, so **Save state automatically** is on there by default and **Prepare ahead** is off.

## If Something Goes Wrong

Open Settings › **Copy diagnostic log** and send it along with a description (see [Troubleshooting](troubleshooting.md)). The log has events and timings, but no proposal text or file names.
