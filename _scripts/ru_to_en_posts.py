#!/usr/bin/env python3
"""
Translate Russian `_ru_posts` into English `_en_posts` using googletrans.

From the repository root:
  pip install -r requirements-translation.txt
  python3 _scripts/ru_to_en_posts.py
  python3 _scripts/fix_en_posts.py

Regenerate the introduction with: python3 _scripts/ru_to_en_posts.py --with-intro
"""
import argparse
import re
import time
from pathlib import Path

from googletrans import Translator

ROOT = Path(__file__).resolve().parents[1]
RU = ROOT / "_ru_posts"
EN = ROOT / "_en_posts"

# (source_ru_file, target_en_file, title_en, date)
INTRO_JOB = (
    "2024-01-01-Introduction.md",
    "00-introduction.md",
    "Introduction",
    "2024-01-01",
)

# (source_ru_file, target_en_file, title_en, date)
CHAPTER_JOBS = [
    ("2024-01-02-Chapter1.md", "01-Chapter1.md", "Chapter 1: Election campaign", "2024-01-02"),
    ("02-Chapter2.md", "02-Chapter2.md", "Chapter 2: District baseline (initial characteristics)", "2024-01-03"),
    ("03-Chapter3.md", "03-Chapter3.md", "Chapter 3: Strategic planning", "2024-01-04"),
    ("04-Chapter4.md", "04-Chapter4.md", "Chapter 4: Candidate preparation", "2024-01-05"),
    ("05-Chapter5.md", "05-Chapter5.md", "Chapter 5: The information wave", "2024-01-06"),
    ("06-Chapter6.md", "06-Chapter6.md", "Chapter 6: Campaign headquarters", "2024-01-07"),
    ("07-Chapter7.md", "07-Chapter7.md", "Chapter 7: Competitors and allies", "2024-01-08"),
    ("08-Chapter8.md", "08-Chapter8.md", "Chapter 8: Volunteers and canvassers", "2024-01-09"),
    ("09-Chapter9.md", "09-Chapter9.md", "Chapter 9: Meetings with voters", "2024-01-10"),
    ("10-Chapter10.md", "10-Chapter10.md", "Chapter 10: Election day", "2024-01-11"),
    ("11-Chapter11.md", "11-Chapter11.md", "Chapter 11: Advertising and selected bibliography", "2024-01-12"),
]

CHUNK = 3500
SLEEP = 0.35


def extract_body(text: str) -> str:
    if not text.strip().startswith("---"):
        return text
    m = re.match(r"^---\n.*?\n---\n", text, re.DOTALL)
    if not m:
        return text
    return text[m.end() :].lstrip("\n")


def chunk_text(s: str) -> list[str]:
    if len(s) <= CHUNK:
        return [s]
    out = []
    start = 0
    n = len(s)
    while start < n:
        end = min(start + CHUNK, n)
        if end < n:
            # break at paragraph or newline
            br = s.rfind("\n\n", start, end)
            if br == -1 or br <= start:
                br = s.rfind("\n", start, end)
            if br > start:
                end = br
        out.append(s[start:end])
        start = end
    return out


def main():
    ap = argparse.ArgumentParser(description="Translate _ru_posts → _en_posts (googletrans).")
    ap.add_argument(
        "--with-intro",
        action="store_true",
        help="Also translate 2024-01-01-Introduction.md → 00-introduction.md (before chapter jobs).",
    )
    args = ap.parse_args()
    jobs = [INTRO_JOB, *CHAPTER_JOBS] if args.with_intro else list(CHAPTER_JOBS)

    t = Translator()
    for src_name, dst_name, title, date in jobs:
        path_ru = RU / src_name
        text = path_ru.read_text(encoding="utf-8")
        body = extract_body(text)
        parts = chunk_text(body)
        eng_parts = []
        for i, p in enumerate(parts):
            if not p.strip():
                eng_parts.append(p)
                continue
            for attempt in range(3):
                try:
                    r = t.translate(p, dest="en", src="ru")
                    eng_parts.append(r.text)
                    break
                except Exception as e:
                    print(f"retry {src_name} chunk {i+1}/{len(parts)}: {e}")
                    time.sleep(2.0 * (attempt + 1))
            else:
                eng_parts.append(f"[translation failed for chunk {i+1}]")
            time.sleep(SLEEP)
        en_body = eng_parts[0] if len(eng_parts) == 1 else "\n\n".join(eng_parts)
        front = (
            f'---\nlayout: chapter\ntitle: "{title}"\ndate: {date}\n'
            f"categories: chapter\nlang: en\ncollection: en_posts\n---\n\n"
        )
        (EN / dst_name).write_text(front + en_body.strip() + "\n", encoding="utf-8")
        print("OK", dst_name, len(parts), "chunks")


if __name__ == "__main__":
    main()
