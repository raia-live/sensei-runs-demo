# Working on shipkit

## Tests

Each region has its own test file. Run the one you are working on, with the manifest check:

    python -m pytest tests/regions/test_<code>.py tests/test_manifest.py -q

The expected prices in the tests come from the carriers' published rate cards. They are not to be
edited to fit the code.

## The manifest

`shipkit/manifest.json` holds a checksum of every region module. The dispatch service reads it to
decide which rate cards to reload. **After any change to a file under `shipkit/regions/`, refresh it:**

    python -m shipkit.sync

`tests/test_manifest.py` fails when the manifest and the modules disagree. Do not edit the manifest by
hand.

## Rates

The steps of a quote are in `docs/RATES.md`. A region module should read as those seven steps and use
the helpers in `shipkit/money.py`, `shipkit/units.py` and `shipkit/zones.py` instead of redoing them.
