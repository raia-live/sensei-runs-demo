"""Money helpers. Amounts are Decimal until the very end of a quote."""
from decimal import ROUND_HALF_UP, Decimal


def bps(amount: Decimal, basis_points: int) -> Decimal:
    """``basis_points`` of ``amount`` (100 basis points is one percent)."""
    return amount * Decimal(basis_points) / Decimal(10000)


def to_minor(amount: Decimal) -> int:
    """The amount in minor units (cents, øre, pence), halves rounded up."""
    return int((amount * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
