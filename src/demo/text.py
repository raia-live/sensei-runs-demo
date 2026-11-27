import re


def slugify(text: str) -> str:
    """Lowercase, words joined by single hyphens, no leading or trailing hyphens."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in text."""
    return len(text.split())
