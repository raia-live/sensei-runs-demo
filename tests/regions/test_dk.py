"""Denmark (DK): prices from the carrier's rate card, in minor units of DKK."""
import pytest

from shipkit import Parcel, quote

CASES = [
    ('small', Parcel(400, 20, 15, 10), '0150', 8344),
    ('heavy', Parcel(5300, 40, 30, 20), '0150', 14708),
    ('bulky-light', Parcel(1200, 60, 40, 40), '0150', 37618),
    ('remote', Parcel(2100, 25, 20, 15), '9612', 18432),
    ('remote-typed-loosely', Parcel(3400, 30, 20, 20), '8 810', 19705),
    ('bulky-remote', Parcel(900, 50, 50, 40), '9612', 46434),
]


@pytest.mark.parametrize("name, parcel, postcode, expected", CASES, ids=[c[0] for c in CASES])
def test_quote(name, parcel, postcode, expected):
    assert quote("dk", parcel, postcode) == expected
