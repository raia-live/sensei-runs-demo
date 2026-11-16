from demo import slugify, word_count


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_strips_edge_hyphens():
    assert slugify("  Hello, World!  ") == "hello-world"


def test_slugify_collapses_punctuation():
    assert slugify("a -- b") == "a-b"


def test_word_count():
    assert word_count("one two  three") == 3
