"""Switzerland (CH): prices from the carrier's rate card, in minor units of CHF."""
import pytest

from shipkit import Parcel, quote

CASES = [
    ('small', Parcel(400, 20, 15, 10), '0150', 740),
    ('heavy', Parcel(5300, 40, 30, 20), '0150', 1817),
    ('bulky-light', Parcel(1200, 60, 40, 40), '0150', 5696),
    ('remote', Parcel(2100, 25, 20, 15), '9112', 2161),
    ('remote-typed-loosely', Parcel(3400, 30, 20, 20), '8 210', 2376),
    ('bulky-remote', Parcel(900, 50, 50, 40), '9112', 6901),
]


@pytest.mark.parametrize("name, parcel, postcode, expected", CASES, ids=[c[0] for c in CASES])
def test_quote(name, parcel, postcode, expected):
    assert quote("ch", parcel, postcode) == expected
