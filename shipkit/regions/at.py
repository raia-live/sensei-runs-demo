"""Parcel quotes for Austria (AT), in minor units of EUR."""
from decimal import Decimal

from shipkit import money, units

CURRENCY = "EUR"
BASE = Decimal("5.20")
PER_KG = Decimal("2.30")
VOLUME_DIVISOR = 5000
REMOTE_PREFIXES = ('92', '74')
REMOTE_FEE = Decimal("7.50")
FUEL_BPS = 725
TAX_BPS = 2000


def quote(parcel: units.Parcel, postcode: str) -> int:
    grams = units.billable_grams(parcel, VOLUME_DIVISOR)
    freight = BASE + PER_KG * units.started_kg(grams)
    if postcode.startswith(REMOTE_PREFIXES):
        freight += REMOTE_FEE
    fuel = money.bps(freight, FUEL_BPS)
    tax = money.bps(freight + fuel, TAX_BPS)
    return money.to_minor(freight + fuel + tax)
