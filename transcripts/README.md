# Transcripts

Real transcripts of Oren John videos go here, one file per video: `<videoId>_<short-title>.md`.

The cloud environment blocks youtube.com and transcript sites, so they can't be pulled automatically yet. Two ways to fill this folder:

1. **Open the network (best).** Add `youtube.com` and `www.youtube.com` to Allowed domains in the environment's Network access settings ([docs](https://code.claude.com/docs/en/cloud-environments#network-access)). Then start a new session and ask Claude to pull transcripts with `youtube-transcript-api` (installs from PyPI, which is already allowed).
2. **By hand.** Paste a video URL into a free tool (tactiq.io/tools/youtube-transcript, youtubetotranscript.com) or use YouTube's "Show transcript", and save the text here or in Drive.

The priority queue is the table in `research/oren-john-notes.md`, section 5. Once transcripts land, re-run the audit against them and update `strategy/01-audit.md` wherever the videos add detail the written material lacked.
