"""Parcel quotes for Greece (GR), in minor units of EUR."""
from decimal import Decimal

from shipkit import money, units, zones

CURRENCY = "EUR"
BASE = Decimal("8.80")
PER_KG = Decimal("2.80")
VOLUME_DIVISOR = 6000
REMOTE_PREFIXES = ('93', '81')
REMOTE_FEE = Decimal("6.00")
FUEL_BPS = 875
TAX_BPS = 2400


def quote(parcel: units.Parcel, postcode: str) -> int:
    grams = parcel.weight_g
    freight = BASE + PER_KG * units.started_kg(grams)
    if zones.is_remote(postcode, REMOTE_PREFIXES):
        freight += REMOTE_FEE
    fuel = money.bps(freight, FUEL_BPS)
    tax = money.bps(freight + fuel, TAX_BPS)
    return money.to_minor(freight + fuel + tax)
