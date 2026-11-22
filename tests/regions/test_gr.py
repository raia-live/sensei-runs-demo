"""Greece (GR): prices from the carrier's rate card, in minor units of EUR."""
import pytest

from shipkit import Parcel, quote

CASES = [
    ('small', Parcel(400, 20, 15, 10), '0150', 1564),
    ('heavy', Parcel(5300, 40, 30, 20), '0150', 3452),
    ('bulky-light', Parcel(1200, 60, 40, 40), '0150', 7228),
    ('remote', Parcel(2100, 25, 20, 15), '9312', 3129),
    ('remote-typed-loosely', Parcel(3400, 30, 20, 20), '8 110', 3506),
    ('bulky-remote', Parcel(900, 50, 50, 40), '9312', 8415),
]


@pytest.mark.parametrize("name, parcel, postcode, expected", CASES, ids=[c[0] for c in CASES])
def test_quote(name, parcel, postcode, expected):
    assert quote("gr", parcel, postcode) == expected
