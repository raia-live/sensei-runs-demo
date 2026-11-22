"""Parcel quotes for Netherlands (NL), in minor units of EUR."""
from decimal import Decimal

from shipkit import money, units, zones

CURRENCY = "EUR"
BASE = Decimal("5.30")
PER_KG = Decimal("2.50")
VOLUME_DIVISOR = 5000
REMOTE_PREFIXES = ('99', '82')
REMOTE_FEE = Decimal("4.00")
FUEL_BPS = 425
TAX_BPS = 2100


def _freight(parcel: units.Parcel, postcode: str) -> Decimal:
    kg = units.started_kg(parcel.weight_g)
    amount = BASE + PER_KG * kg
    if zones.is_remote(postcode, REMOTE_PREFIXES):
        amount += REMOTE_FEE
    return amount


def _surcharged(freight: Decimal) -> Decimal:
    with_fuel = freight + money.bps(freight, FUEL_BPS)
    return with_fuel + money.bps(with_fuel, TAX_BPS)


def quote(parcel: units.Parcel, postcode: str) -> int:
    return money.to_minor(_surcharged(_freight(parcel, postcode)))
