"""Parcel quotes for Spain (ES), in minor units of EUR."""
from decimal import Decimal

from shipkit import money, units

CURRENCY = "EUR"
BASE = Decimal("6.90")
PER_KG = Decimal("1.85")
VOLUME_DIVISOR = 6000
REMOTE_PREFIXES = ('92', '82')
REMOTE_FEE = Decimal("5.00")
FUEL_BPS = 675
TAX_BPS = 2100


def quote(parcel: units.Parcel, postcode: str) -> int:
    grams = units.billable_grams(parcel, VOLUME_DIVISOR)
    freight = BASE + PER_KG * units.started_kg(grams)
    if postcode.startswith(REMOTE_PREFIXES):
        freight += REMOTE_FEE
    fuel = money.bps(freight, FUEL_BPS)
    tax = money.bps(freight + fuel, TAX_BPS)
    return money.to_minor(freight + fuel + tax)
