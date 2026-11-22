from shipkit import zones


def test_normalise():
    assert zones.normalise(" iv2 3ab ") == "IV23AB"
    assert zones.normalise("8 4-10") == "8410"


def test_is_remote():
    assert zones.is_remote("9 012", ("90", "84"))
    assert not zones.is_remote("0150", ("90", "84"))
