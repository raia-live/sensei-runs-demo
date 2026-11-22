from shipkit.units import Parcel, billable_grams, started_kg, volumetric_grams


def test_volumetric():
    assert volumetric_grams(Parcel(1000, 50, 40, 30), 5000) == 12000


def test_billable_is_the_greater():
    assert billable_grams(Parcel(1000, 50, 40, 30), 5000) == 12000
    assert billable_grams(Parcel(15000, 50, 40, 30), 5000) == 15000


def test_started_kg():
    assert started_kg(1) == 1
    assert started_kg(1000) == 1
    assert started_kg(1001) == 2
