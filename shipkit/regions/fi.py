"""Parcel quotes for Finland (FI), in minor units of EUR."""
from decimal import Decimal

from shipkit import money, units, zones

CURRENCY = "EUR"
BASE = Decimal("4.40")
PER_KG = Decimal("2.75")
VOLUME_DIVISOR = 4000
REMOTE_PREFIXES = ('95', '83')
REMOTE_FEE = Decimal("5.00")
FUEL_BPS = 775
TAX_BPS = 2550


def quote(parcel: units.Parcel, postcode: str) -> int:
    grams = parcel.weight_g
    freight = BASE + PER_KG * units.started_kg(grams)
    if zones.is_remote(postcode, REMOTE_PREFIXES):
        freight += REMOTE_FEE
    fuel = money.bps(freight, FUEL_BPS)
    tax = money.bps(freight + fuel, TAX_BPS)
    return money.to_minor(freight + fuel + tax)
