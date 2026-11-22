"""shipkit: parcel quotes by region."""
from shipkit.units import Parcel

__all__ = ["Parcel", "quote"]


def quote(region: str, parcel: Parcel, postcode: str) -> int:
    """The price of sending ``parcel`` to ``postcode`` in ``region``, in minor units."""
    from shipkit import regions

    return regions.load(region).quote(parcel, postcode)
