"""Poland (PL): prices from the carrier's rate card, in minor units of PLN."""
import pytest

from shipkit import Parcel, quote

CASES = [
    ('small', Parcel(400, 20, 15, 10), '0150', 5514),
    ('heavy', Parcel(5300, 40, 30, 20), '0150', 12770),
    ('bulky-light', Parcel(1200, 60, 40, 40), '0150', 38889),
    ('remote', Parcel(2100, 25, 20, 15), '9512', 11055),
    ('remote-typed-loosely', Parcel(3400, 30, 20, 20), '8 310', 12506),
    ('bulky-remote', Parcel(900, 50, 50, 40), '9512', 42979),
]


@pytest.mark.parametrize("name, parcel, postcode, expected", CASES, ids=[c[0] for c in CASES])
def test_quote(name, parcel, postcode, expected):
    assert quote("pl", parcel, postcode) == expected
