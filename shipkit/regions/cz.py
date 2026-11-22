"""Parcel quotes for Czechia (CZ), in minor units of CZK."""
from decimal import Decimal

from shipkit import money, units, zones

CURRENCY = "CZK"
BASE = Decimal("132.50")
PER_KG = Decimal("46.25")
VOLUME_DIVISOR = 4000
REMOTE_PREFIXES = ('91', '82')
REMOTE_FEE = Decimal("75.00")
FUEL_BPS = 575
TAX_BPS = 2100


def quote(parcel: units.Parcel, postcode: str) -> int:
    grams = units.billable_grams(parcel, VOLUME_DIVISOR)
    freight = BASE + PER_KG * units.started_kg(grams)
    if zones.is_remote(postcode, REMOTE_PREFIXES):
        freight += REMOTE_FEE
    fuel = money.bps(freight, FUEL_BPS)
    tax = money.bps(freight + fuel, TAX_BPS)
    return int((freight + fuel + tax) * 100)
