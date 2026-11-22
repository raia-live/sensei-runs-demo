"""Portugal (PT): prices from the carrier's rate card, in minor units of EUR."""
import pytest

from shipkit import Parcel, quote

CASES = [
    ('small', Parcel(400, 20, 15, 10), '0150', 827),
    ('heavy', Parcel(5300, 40, 30, 20), '0150', 1812),
    ('bulky-light', Parcel(1200, 60, 40, 40), '0150', 3782),
    ('remote', Parcel(2100, 25, 20, 15), '9912', 1681),
    ('remote-typed-loosely', Parcel(3400, 30, 20, 20), '8 510', 1878),
    ('bulky-remote', Parcel(900, 50, 50, 40), '9912', 4438),
]


@pytest.mark.parametrize("name, parcel, postcode, expected", CASES, ids=[c[0] for c in CASES])
def test_quote(name, parcel, postcode, expected):
    assert quote("pt", parcel, postcode) == expected
