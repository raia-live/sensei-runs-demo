"""Netherlands (NL): prices from the carrier's rate card, in minor units of EUR."""
import pytest

from shipkit import Parcel, quote

CASES = [
    ('small', Parcel(400, 20, 15, 10), '0150', 984),
    ('heavy', Parcel(5300, 40, 30, 20), '0150', 2561),
    ('bulky-light', Parcel(1200, 60, 40, 40), '0150', 6976),
    ('remote', Parcel(2100, 25, 20, 15), '9912', 2119),
    ('remote-typed-loosely', Parcel(3400, 30, 20, 20), '8 210', 2435),
    ('bulky-remote', Parcel(900, 50, 50, 40), '9912', 7480),
]


@pytest.mark.parametrize("name, parcel, postcode, expected", CASES, ids=[c[0] for c in CASES])
def test_quote(name, parcel, postcode, expected):
    assert quote("nl", parcel, postcode) == expected
