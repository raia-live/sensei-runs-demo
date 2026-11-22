"""Parcel quotes for Poland (PL), in minor units of PLN."""
from decimal import Decimal

from shipkit import money, units, zones

CURRENCY = "PLN"
BASE = Decimal("30.80")
PER_KG = Decimal("11.00")
VOLUME_DIVISOR = 4000
REMOTE_PREFIXES = ('95', '83')
REMOTE_FEE = Decimal("20.00")
FUEL_BPS = 725
TAX_BPS = 2300


def quote(parcel: units.Parcel, postcode: str) -> int:
    grams = units.billable_grams(parcel, VOLUME_DIVISOR)
    freight = BASE + PER_KG * units.started_kg(grams)
    if zones.is_remote(postcode, REMOTE_PREFIXES):
        freight += REMOTE_FEE
    fuel = money.bps(freight, FUEL_BPS)
    tax = money.bps(freight, TAX_BPS)
    return money.to_minor(freight + fuel + tax)
