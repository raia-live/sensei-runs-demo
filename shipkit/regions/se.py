"""Parcel quotes for Sweden (SE), in minor units of SEK."""
from decimal import Decimal

from shipkit import money, units

CURRENCY = "SEK"
BASE = Decimal("74.00")
PER_KG = Decimal("19.00")
VOLUME_DIVISOR = 4000
REMOTE_PREFIXES = ('96', '78')
REMOTE_FEE = Decimal("85.00")
FUEL_BPS = 825
TAX_BPS = 2500


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
