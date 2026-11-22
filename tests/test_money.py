from decimal import Decimal

from shipkit import money


def test_bps():
    assert money.bps(Decimal("200.00"), 650) == Decimal("13.00")


def test_to_minor_rounds_halves_up():
    assert money.to_minor(Decimal("10.005")) == 1001
    assert money.to_minor(Decimal("10.004")) == 1000
