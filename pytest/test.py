from main import inc, dec, join_str

def test_incr_case01():
    assert inc(3) == 4

def test_dec_case01():
    assert dec(3) == 2

def test_join_str_case01():
    assert join_str("2020", "XYZ") == "2020/XYZ"

