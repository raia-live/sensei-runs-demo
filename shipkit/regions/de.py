"""Parcel quotes for Germany (DE), in minor units of EUR."""
from decimal import Decimal

from shipkit import money, units, zones

CURRENCY = "EUR"
BASE = Decimal("9.00")
PER_KG = Decimal("1.00")
VOLUME_DIVISOR = 6000
REMOTE_PREFIXES = ('96', '85')
REMOTE_FEE = Decimal("3.50")
FUEL_BPS = 775
TAX_BPS = 1900


def quote(parcel: units.Parcel, postcode: str) -> int:
    grams = parcel.weight_g
    freight = BASE + PER_KG * units.started_kg(grams)
    if zones.is_remote(postcode, REMOTE_PREFIXES):
        freight += REMOTE_FEE
    fuel = money.bps(freight, FUEL_BPS)
    tax = money.bps(freight + fuel, TAX_BPS)
    return money.to_minor(freight + fuel + tax)
