"""Parcel quotes for Norway (NO), in minor units of NOK."""
from decimal import Decimal

from shipkit import money, units, zones

CURRENCY = "NOK"
BASE = Decimal("75.00")
PER_KG = Decimal("25.50")
VOLUME_DIVISOR = 4000
REMOTE_PREFIXES = ('96', '71')
REMOTE_FEE = Decimal("40.00")
FUEL_BPS = 725
TAX_BPS = 2500


def quote(parcel: units.Parcel, postcode: str) -> int:
    grams = units.billable_grams(parcel, VOLUME_DIVISOR)
    freight = BASE + PER_KG * units.started_kg(grams)
    if zones.is_remote(postcode, REMOTE_PREFIXES):
        freight += REMOTE_FEE
    fuel = money.bps(freight, FUEL_BPS)
    tax = money.bps(freight + fuel, TAX_BPS)
    return int((freight + fuel + tax) * 100)
