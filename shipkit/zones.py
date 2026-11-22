"""Postcodes. People type them every way there is."""
import re


def normalise(postcode: str) -> str:
    """Upper case, with everything but letters and digits removed."""
    return re.sub(r"[^0-9A-Z]", "", postcode.upper())


def is_remote(postcode: str, prefixes: tuple[str, ...]) -> bool:
    """Whether the postcode, as normalised, starts with one of ``prefixes``."""
    return normalise(postcode).startswith(tuple(prefixes))
