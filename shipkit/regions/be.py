"""Parcel quotes for Belgium (BE), in minor units of EUR."""
from decimal import Decimal

from shipkit import money, units, zones

CURRENCY = "EUR"
BASE = Decimal("4.50")
PER_KG = Decimal("2.35")
VOLUME_DIVISOR = 4000
REMOTE_PREFIXES = ('95', '84')
REMOTE_FEE = Decimal("8.50")
FUEL_BPS = 525
TAX_BPS = 2100


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
