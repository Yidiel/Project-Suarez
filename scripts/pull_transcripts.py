"""Pull transcripts for the videos listed in transcripts/QUEUE.md.

Needs youtube.com allowed in the environment's network settings.
    pip install youtube-transcript-api
    python3 scripts/pull_transcripts.py            # starred videos first, then the rest
    python3 scripts/pull_transcripts.py --top      # starred only
"""
import pathlib
import re
import sys

from youtube_transcript_api import YouTubeTranscriptApi

ROOT = pathlib.Path(__file__).resolve().parent.parent
QUEUE = ROOT / "transcripts" / "QUEUE.md"
OUT = ROOT / "transcripts"

ROW = re.compile(r"^\| (★?) \| \[([\w-]{11})\]\(.*?\) \| (.*?) \| (.*) \|$")


def queue(top_only):
    rows = [m.groups() for m in map(ROW.match, QUEUE.read_text().splitlines()) if m]
    rows.sort(key=lambda r: r[0] != "★")
    return [r for r in rows if r[0] == "★" or not top_only]


def slug(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60]


def main():
    api = YouTubeTranscriptApi()
    for star, vid, length, title in queue("--top" in sys.argv):
        path = OUT / f"{vid}_{slug(title)}.md"
        if path.exists():
            continue
        try:
            segs = api.fetch(vid, languages=["en"])
        except Exception as e:
            print(f"skip {vid}: {type(e).__name__}")
            continue
        lines = [f"# {title}", "", f"https://www.youtube.com/watch?v={vid} · {length}", ""]
        for s in segs:
            m, sec = divmod(int(s.start), 60)
            lines.append(f"[{m:02d}:{sec:02d}] {s.text}")
        path.write_text("\n".join(lines) + "\n")
        print(f"ok {vid} {title}")


if __name__ == "__main__":
    main()
