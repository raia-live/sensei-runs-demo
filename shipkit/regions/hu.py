"""Parcel quotes for Hungary (HU), in minor units of HUF."""
from decimal import Decimal

from shipkit import money, units, zones

CURRENCY = "HUF"
BASE = Decimal("3045.00")
PER_KG = Decimal("507.50")
VOLUME_DIVISOR = 6000
REMOTE_PREFIXES = ('99', '83')
REMOTE_FEE = Decimal("2625.00")
FUEL_BPS = 425
TAX_BPS = 2700


def quote(parcel: units.Parcel, postcode: str) -> int:
    grams = units.billable_grams(parcel, VOLUME_DIVISOR)
    freight = BASE + PER_KG * units.started_kg(grams)
    if zones.is_remote(postcode, REMOTE_PREFIXES):
        freight += REMOTE_FEE
    fuel = money.bps(freight, FUEL_BPS)
    tax = money.bps(freight, TAX_BPS)
    return money.to_minor(freight + fuel + tax)
