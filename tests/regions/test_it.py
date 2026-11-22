"""Italy (IT): prices from the carrier's rate card, in minor units of EUR."""
import pytest

from shipkit import Parcel, quote

CASES = [
    ('small', Parcel(400, 20, 15, 10), '0150', 1327),
    ('heavy', Parcel(5300, 40, 30, 20), '0150', 2853),
    ('bulky-light', Parcel(1200, 60, 40, 40), '0150', 7125),
    ('remote', Parcel(2100, 25, 20, 15), '9312', 2866),
    ('remote-typed-loosely', Parcel(3400, 30, 20, 20), '8 710', 3171),
    ('bulky-remote', Parcel(900, 50, 50, 40), '9312', 8053),
]


@pytest.mark.parametrize("name, parcel, postcode, expected", CASES, ids=[c[0] for c in CASES])
def test_quote(name, parcel, postcode, expected):
    assert quote("it", parcel, postcode) == expected
