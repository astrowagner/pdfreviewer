# Privacy and Data

Proposal Listener has no server and no account, and it uploads nothing. This page says what is stored where, what crosses the network, and how you can check it yourself.

## What Stays on Your Device

Everything you put into the app stays in your browser's storage on your device (IndexedDB, for this site only):

| What | Where |
|---|---|
| Your proposal PDFs, and the text read from them | The app's storage in your browser |
| Highlights, notes, your review, your place, and how much you have heard | The app's storage in your browser |
| Settings | The app's storage in your browser |
| The natural voice's files (about 104 MB), after you choose **Download and turn on** | The browser's storage for this site |
| Speech made by **Prepare ahead** | The browser's storage for this site (up to 1 GB, oldest removed first) |

Nothing here is sent anywhere. **Remove from this device** (the **⋯** button on a proposal) deletes that proposal's PDF, highlights, and notes. Removing the natural voice download removes prepared speech too.

## What Crosses the Network

- **Loading the app.** Your browser downloads `index.html` from GitHub Pages, like any website. GitHub [logs visitors' IP addresses for security purposes](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection). It does not see your proposals, which never leave your device.
- **The natural voice's files,** downloaded once from the same site when you choose **Download and turn on**. They are checked by SHA-256 and kept on the device.
- **Nothing else.** The page's Content Security Policy allows network requests only to its own site (`connect-src 'self'`) and loads no outside scripts, styles, fonts, or images (`default-src 'none'`). There are no analytics and no cookies, and no form can be submitted anywhere (`form-action 'none'`).

## Voices

- **The natural voice** is an AI speech model (Kokoro-82M) that runs inside the page on your device. Your text is not sent to any service.
- **Device voices** are your operating system's voices. Some browsers also offer network voices that send text to a provider, for example Chrome's Google voices. The app marks those "network" and hides them while **On-device voices only** is on, which is the default. On iPhone, the voices Safari offers are on the device.

## Files You Save

Exported files go wherever your browser saves downloads, and from there they are yours to handle:

- The **notes report** contains your notes and short quotes from the proposal. Each page is marked "Confidential: proposal review notes".
- The **annotated proposal** and the **Save state** file contain the proposal PDFs themselves.
- On iPhone, Safari saves downloads to **iCloud Drive** unless you choose **On My iPhone** under iOS Settings › Apps › Safari › Downloads.
- PDF comments are signed "Reviewer" unless you change **Author name on PDF comments** in Settings.

## The Diagnostic Log

Settings › **Copy diagnostic log** copies a log of recent events on this device: timings, error messages, the browser, and the screen size. It contains no proposal text and no file names. It is never sent anywhere; you copy it and share it only if you choose to.

## Your Review Program's Rules

Review programs set their own confidentiality rules. STScI, for example, [forbids reviewers from uploading proposal content or review materials to generative AI tools](https://jwst-docs.stsci.edu/jwst-opportunities-and-policies/past-jwst-proposal-opportunities/jwst-peer-review-information-cycle-4/jwst-peer-review-guide-cycle-4/executive-committee-chairs-and-at-larges-cycle-4). Proposal Listener does not upload anything, and its natural voice runs on your device; still, follow the rules of the program you review for, and ask its contact if you are unsure.

## When the Browser Deletes the App's Data

Browsers can remove a site's stored data. Safari [deletes a site's script-writable storage after seven days of Safari use without visiting the site](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/), and storage cleanups can remove it too. At startup the app asks the browser to keep its data, and Settings › **Data on this device** shows the answer. To be safe, use **Save state** now and then. Inside claude.ai, Safari erases the app's data when it quits.

## Check It Yourself

- **The policy:** view the page source of https://astrowagner.github.io/pdfreviewer/ and find the `Content-Security-Policy` meta tag near the top.
- **The traffic:** open your browser's developer tools, then the Network panel, and use the app. Every request goes to the app's own site.
- **The code:** `index.html` in this repository is the whole app, with its code readable in the file.
