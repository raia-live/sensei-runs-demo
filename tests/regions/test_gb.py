"""United Kingdom (GB): prices from the carrier's rate card, in minor units of GBP."""
import pytest

from shipkit import Parcel, quote

CASES = [
    ('small', Parcel(400, 20, 15, 10), 'SW1A 1AA', 716),
    ('heavy', Parcel(5300, 40, 30, 20), 'SW1A 1AA', 1534),
    ('bulky-light', Parcel(1200, 60, 40, 40), 'SW1A 1AA', 3821),
    ('remote', Parcel(2100, 25, 20, 15), 'BT2 3AB', 1986),
    ('remote-typed-loosely', Parcel(3400, 30, 20, 20), ' ze4 1xy', 2149),
    ('bulky-remote', Parcel(900, 50, 50, 40), 'BT2 3AB', 4764),
]


@pytest.mark.parametrize("name, parcel, postcode, expected", CASES, ids=[c[0] for c in CASES])
def test_quote(name, parcel, postcode, expected):
    assert quote("gb", parcel, postcode) == expected
