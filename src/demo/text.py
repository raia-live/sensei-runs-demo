import re


def slugify(text: str) -> str:
    """Lowercase, words joined by single hyphens, no leading or trailing hyphens."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text


def word_count(text: str) -> int:
    return len(text.split())
