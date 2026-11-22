"""Parcel quotes for United Kingdom (GB), in minor units of GBP."""
from decimal import Decimal

from shipkit import money, units

CURRENCY = "GBP"
BASE = Decimal("4.40")
PER_KG = Decimal("1.30")
VOLUME_DIVISOR = 5000
REMOTE_PREFIXES = ('BT', 'ZE')
REMOTE_FEE = Decimal("7.50")
FUEL_BPS = 475
TAX_BPS = 2000


def _freight(parcel: units.Parcel, postcode: str) -> Decimal:
    kg = units.started_kg(units.billable_grams(parcel, VOLUME_DIVISOR))
    amount = BASE + PER_KG * kg
    if postcode.startswith(REMOTE_PREFIXES):
        amount += REMOTE_FEE
    return amount


def _surcharged(freight: Decimal) -> Decimal:
    with_fuel = freight + money.bps(freight, FUEL_BPS)
    return with_fuel + money.bps(with_fuel, TAX_BPS)


def quote(parcel: units.Parcel, postcode: str) -> int:
    return money.to_minor(_surcharged(_freight(parcel, postcode)))
