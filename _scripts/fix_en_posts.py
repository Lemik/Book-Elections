#!/usr/bin/env python3
"""Post-process machine-translated EN posts: spacing, ИК terms, ch.1 slogan."""
import re
from pathlib import Path

EN = Path(__file__).resolve().parents[1] / "_en_posts"


def fix_text(text: str) -> str:
    # Space after . before caps when glued (e.g. "opponents.During")
    for _ in range(4):
        text = re.sub(r"([a-z,])\s*\.([A-Z])", r"\1. \2", text)
        text = re.sub(r"(\))\s*\.([A-Z])", r"\1. \2", text)
    for _ in range(2):
        text = re.sub(r"([!?])([A-Z])", r"\1 \2", text)
    # IR / IC / EC as Russian ИК (election campaign) — word boundaries
    for a, b in [
        (r"\bIC's\b", "election campaign's"),
        (r"\bIC\b", "election campaign"),
        (r"\bIR\b", "election campaign"),
        (r"\bEC\b", "election campaign"),
    ]:
        text = re.sub(a, b, text)
    # Machine-translation artifacts
    text = text.replace(
        "*An election campaign (election campaign) is",
        "*An election campaign (EC) is",
    )
    text = text.replace(
        "large-scale local electoral commission (from 20 to 50",
        "local large-scale election campaign (from 20 to 50",
    )
    text = text.replace("conducting electoral elections", "conducting election campaigns")
    text = text.replace("referendum.3.", "referendum. 3.")
    # e.g. "voters);regional" -> "voters); regional"
    text = re.sub(r"\);([A-Za-z][A-Za-z\-]*)", r"); \1", text)
    # MT often glues "word;word" in lists: "country;actions" -> "country; actions"
    for _ in range(5):
        n = re.sub(r"([A-Za-z0-9\)]);([A-Za-z])", r"\1; \2", text)
        if n == text:
            break
        text = n
    # e.g. "win";negative" or "…");negative" — any ; directly before a letter
    text = re.sub(r";(?=[A-Za-z])", "; ", text)
    # “swamp”.The (missing space after period)
    for _ in range(2):
        text = re.sub(r"”\.([A-Z])", r"”. \1", text)
        text = re.sub(r'"\.([A-Z])', r'". \1', text)
    return text


def main():
    for path in sorted(EN.glob("*.md")):
        if path.name == "00-introduction.md":
            raw = path.read_text(encoding="utf-8")
            # Fix only spacing in hand-written intro
            if "---" in raw:
                parts = raw.split("---", 2)
                if len(parts) >= 3:
                    body = fix_text(parts[2])
                    raw = f"---{parts[1]}---\n" + body
            path.write_text(raw, encoding="utf-8")
            continue
        raw = path.read_text(encoding="utf-8")
        parts = raw.split("---", 2)
        if len(parts) < 3:
            continue
        fm, body = parts[0] + "---" + parts[1] + "---\n", parts[2]
        body = fix_text(body)
        if path.name == "01-Chapter1.md":
            body = body.replace(
                "then in Ukraine the next elections will be held under the slogan: “Vote, or you win!”",
                "then the next elections in Ukraine will be held under the slogan: “Vote, or your neighbor wins!”",
            )
        path.write_text(fm + body, encoding="utf-8")
        print("fixed", path.name)


if __name__ == "__main__":
    main()
