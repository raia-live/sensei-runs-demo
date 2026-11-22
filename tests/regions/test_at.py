"""Austria (AT): prices from the carrier's rate card, in minor units of EUR."""
import pytest

from shipkit import Parcel, quote

CASES = [
    ('small', Parcel(400, 20, 15, 10), '0150', 965),
    ('heavy', Parcel(5300, 40, 30, 20), '0150', 2445),
    ('bulky-light', Parcel(1200, 60, 40, 40), '0150', 6589),
    ('remote', Parcel(2100, 25, 20, 15), '9212', 2523),
    ('remote-typed-loosely', Parcel(3400, 30, 20, 20), '7 410', 2819),
    ('bulky-remote', Parcel(900, 50, 50, 40), '9212', 7555),
]


@pytest.mark.parametrize("name, parcel, postcode, expected", CASES, ids=[c[0] for c in CASES])
def test_quote(name, parcel, postcode, expected):
    assert quote("at", parcel, postcode) == expected
