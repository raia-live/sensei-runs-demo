"""Parcel quotes for Italy (IT), in minor units of EUR."""
from decimal import Decimal

from shipkit import money, units, zones

CURRENCY = "EUR"
BASE = Decimal("7.70")
PER_KG = Decimal("2.30")
VOLUME_DIVISOR = 5000
REMOTE_PREFIXES = ('93', '87')
REMOTE_FEE = Decimal("7.00")
FUEL_BPS = 875
TAX_BPS = 2200


def _freight(parcel: units.Parcel, postcode: str) -> Decimal:
    kg = units.started_kg(units.billable_grams(parcel, VOLUME_DIVISOR))
    amount = BASE + PER_KG * kg
    if zones.is_remote(postcode, REMOTE_PREFIXES):
        amount += REMOTE_FEE
    return amount


def _surcharged(freight: Decimal) -> Decimal:
    with_fuel = freight + money.bps(freight, FUEL_BPS)
    return with_fuel + money.bps(with_fuel, TAX_BPS)


def quote(parcel: units.Parcel, postcode: str) -> int:
    return int(_surcharged(_freight(parcel, postcode)) * 100)
