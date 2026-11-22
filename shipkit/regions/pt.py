"""Parcel quotes for Portugal (PT), in minor units of EUR."""
from decimal import Decimal

from shipkit import money, units, zones

CURRENCY = "EUR"
BASE = Decimal("4.80")
PER_KG = Decimal("1.50")
VOLUME_DIVISOR = 6000
REMOTE_PREFIXES = ('99', '85')
REMOTE_FEE = Decimal("3.50")
FUEL_BPS = 675
TAX_BPS = 2300


def _freight(parcel: units.Parcel, postcode: str) -> Decimal:
    kg = units.started_kg(units.billable_grams(parcel, VOLUME_DIVISOR))
    amount = BASE + PER_KG * kg
    if zones.is_remote(postcode, REMOTE_PREFIXES):
        amount += REMOTE_FEE
    return amount


def _surcharged(freight: Decimal) -> Decimal:
    with_fuel = freight + money.bps(freight, FUEL_BPS)
    return with_fuel + money.bps(freight, TAX_BPS)


def quote(parcel: units.Parcel, postcode: str) -> int:
    return money.to_minor(_surcharged(_freight(parcel, postcode)))
