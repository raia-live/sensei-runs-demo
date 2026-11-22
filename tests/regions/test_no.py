"""Norway (NO): prices from the carrier's rate card, in minor units of NOK."""
import pytest

from shipkit import Parcel, quote

CASES = [
    ('small', Parcel(400, 20, 15, 10), '0150', 13473),
    ('heavy', Parcel(5300, 40, 30, 20), '0150', 30566),
    ('bulky-light', Parcel(1200, 60, 40, 40), '0150', 92101),
    ('remote', Parcel(2100, 25, 20, 15), '9612', 25673),
    ('remote-typed-loosely', Parcel(3400, 30, 20, 20), '7 110', 29092),
    ('bulky-remote', Parcel(900, 50, 50, 40), '9612', 100882),
]


@pytest.mark.parametrize("name, parcel, postcode, expected", CASES, ids=[c[0] for c in CASES])
def test_quote(name, parcel, postcode, expected):
    assert quote("no", parcel, postcode) == expected
