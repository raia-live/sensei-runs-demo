"""Ireland (IE): prices from the carrier's rate card, in minor units of EUR."""
import pytest

from shipkit import Parcel, quote

CASES = [
    ('small', Parcel(400, 20, 15, 10), 'D02 X285', 1524),
    ('heavy', Parcel(5300, 40, 30, 20), 'D02 X285', 2744),
    ('bulky-light', Parcel(1200, 60, 40, 40), 'D02 X285', 7137),
    ('remote', Parcel(2100, 25, 20, 15), 'P72 3AB', 2539),
    ('remote-typed-loosely', Parcel(3400, 30, 20, 20), ' h54 1xy', 2783),
    ('bulky-remote', Parcel(900, 50, 50, 40), 'P72 3AB', 7908),
]


@pytest.mark.parametrize("name, parcel, postcode, expected", CASES, ids=[c[0] for c in CASES])
def test_quote(name, parcel, postcode, expected):
    assert quote("ie", parcel, postcode) == expected
