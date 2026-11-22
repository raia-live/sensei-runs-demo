"""Refresh ``shipkit/manifest.json`` from the region modules.

    python -m shipkit.sync           write the manifest
    python -m shipkit.sync --check   exit 1 when it is out of date

The dispatch service reads the manifest to decide which rate cards to reload,
so it has to match the modules exactly.
"""
import hashlib
import importlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
MANIFEST = HERE / "manifest.json"


def build() -> dict:
    regions = {}
    for path in sorted((HERE / "regions").glob("*.py")):
        if path.name == "__init__.py":
            continue
        module = importlib.import_module(f"shipkit.regions.{path.stem}")
        regions[path.stem] = {
            "currency": module.CURRENCY,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
    return {"version": 1, "regions": regions}


def stale() -> list[str]:
    want = build()["regions"]
    have = json.loads(MANIFEST.read_text())["regions"] if MANIFEST.exists() else {}
    return sorted(code for code in set(want) | set(have) if want.get(code) != have.get(code))


def main(argv: list[str]) -> int:
    if "--check" in argv:
        out = stale()
        if out:
            print("out of date:", ", ".join(out))
        return 1 if out else 0
    MANIFEST.write_text(json.dumps(build(), indent=2, sort_keys=True) + "\n")
    print(f"wrote {MANIFEST.relative_to(HERE.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
