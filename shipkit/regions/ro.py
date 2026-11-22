"""Parcel quotes for Romania (RO), in minor units of RON."""
from decimal import Decimal

from shipkit import money, units

CURRENCY = "RON"
BASE = Decimal("26.50")
PER_KG = Decimal("12.25")
VOLUME_DIVISOR = 6000
REMOTE_PREFIXES = ('91', '83')
REMOTE_FEE = Decimal("25.00")
FUEL_BPS = 725
TAX_BPS = 1900


def quote(parcel: units.Parcel, postcode: str) -> int:
    grams = units.billable_grams(parcel, VOLUME_DIVISOR)
    freight = BASE + PER_KG * units.started_kg(grams)
    if postcode.startswith(REMOTE_PREFIXES):
        freight += REMOTE_FEE
    fuel = money.bps(freight, FUEL_BPS)
    tax = money.bps(freight + fuel, TAX_BPS)
    return money.to_minor(freight + fuel + tax)
