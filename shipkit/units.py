"""Parcels and the weight a carrier bills for."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Parcel:
    weight_g: int
    length_cm: int
    width_cm: int
    height_cm: int


def volumetric_grams(parcel: Parcel, divisor: int) -> int:
    """The weight a parcel of this size is billed as: cm3 / divisor, in kg."""
    cm3 = parcel.length_cm * parcel.width_cm * parcel.height_cm
    return -(-cm3 * 1000 // divisor)


def billable_grams(parcel: Parcel, divisor: int) -> int:
    """The greater of what the parcel weighs and what its size is billed as."""
    return max(parcel.weight_g, volumetric_grams(parcel, divisor))


def started_kg(grams: int) -> int:
    """Kilograms, counting a started kilogram as a whole one."""
    return -(-grams // 1000)
