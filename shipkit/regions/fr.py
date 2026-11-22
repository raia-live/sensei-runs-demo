"""Parcel quotes for France (FR), in minor units of EUR."""
from decimal import Decimal

from shipkit import money, units, zones

CURRENCY = "EUR"
BASE = Decimal("5.30")
PER_KG = Decimal("2.10")
VOLUME_DIVISOR = 5000
REMOTE_PREFIXES = ('96', '86')
REMOTE_FEE = Decimal("4.50")
FUEL_BPS = 825
TAX_BPS = 2000


def quote(parcel: units.Parcel, postcode: str) -> int:
    grams = units.billable_grams(parcel, VOLUME_DIVISOR)
    freight = BASE + PER_KG * units.started_kg(grams)
    if zones.is_remote(postcode, REMOTE_PREFIXES):
        freight += REMOTE_FEE
    fuel = money.bps(freight, FUEL_BPS)
    tax = money.bps(freight, TAX_BPS)
    return money.to_minor(freight + fuel + tax)
