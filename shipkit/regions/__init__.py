"""One module per region. Each has ``CURRENCY`` and ``quote(parcel, postcode)``."""
import importlib
from pathlib import Path


def available() -> list[str]:
    return sorted(p.stem for p in Path(__file__).parent.glob("*.py") if p.name != "__init__.py")


def load(code: str):
    return importlib.import_module(f"shipkit.regions.{code.lower()}")
