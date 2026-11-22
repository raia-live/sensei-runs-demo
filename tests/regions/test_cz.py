"""Czechia (CZ): prices from the carrier's rate card, in minor units of CZK."""
import pytest

from shipkit import Parcel, quote

CASES = [
    ('small', Parcel(400, 20, 15, 10), '0150', 22872),
    ('heavy', Parcel(5300, 40, 30, 20), '0150', 52463),
    ('bulky-light', Parcel(1200, 60, 40, 40), '0150', 158987),
    ('remote', Parcel(2100, 25, 20, 15), '9112', 44305),
    ('remote-typed-loosely', Parcel(3400, 30, 20, 20), '8 210', 50223),
    ('bulky-remote', Parcel(900, 50, 50, 40), '9112', 174502),
]


@pytest.mark.parametrize("name, parcel, postcode, expected", CASES, ids=[c[0] for c in CASES])
def test_quote(name, parcel, postcode, expected):
    assert quote("cz", parcel, postcode) == expected
