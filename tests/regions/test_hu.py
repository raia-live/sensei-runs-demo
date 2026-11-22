"""Hungary (HU): prices from the carrier's rate card, in minor units of HUF."""
import pytest

from shipkit import Parcel, quote

CASES = [
    ('small', Parcel(400, 20, 15, 10), '0150', 470342),
    ('heavy', Parcel(5300, 40, 30, 20), '0150', 806301),
    ('bulky-light', Parcel(1200, 60, 40, 40), '0150', 1478218),
    ('remote', Parcel(2100, 25, 20, 15), '9912', 952269),
    ('remote-typed-loosely', Parcel(3400, 30, 20, 20), '8 310', 1019461),
    ('bulky-remote', Parcel(900, 50, 50, 40), '9912', 1892953),
]


@pytest.mark.parametrize("name, parcel, postcode, expected", CASES, ids=[c[0] for c in CASES])
def test_quote(name, parcel, postcode, expected):
    assert quote("hu", parcel, postcode) == expected
