"""Parcel quotes for Ireland (IE), in minor units of EUR."""
from decimal import Decimal

from shipkit import money, units, zones

CURRENCY = "EUR"
BASE = Decimal("9.70")
PER_KG = Decimal("1.85")
VOLUME_DIVISOR = 4000
REMOTE_PREFIXES = ('P7', 'H5')
REMOTE_FEE = Decimal("4.00")
FUEL_BPS = 725
TAX_BPS = 2300


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
