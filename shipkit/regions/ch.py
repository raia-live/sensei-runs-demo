"""Parcel quotes for Switzerland (CH), in minor units of CHF."""
from decimal import Decimal

from shipkit import money, units, zones

CURRENCY = "CHF"
BASE = Decimal("4.50")
PER_KG = Decimal("1.85")
VOLUME_DIVISOR = 4000
REMOTE_PREFIXES = ('91', '82')
REMOTE_FEE = Decimal("8.50")
FUEL_BPS = 775
TAX_BPS = 810


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
