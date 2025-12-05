from src.main import elevar, sumar, to_upper, to_lower
def test_elevar():
    assert elevar(2,3) == 8

def test_sumar():
    assert sumar(2,5) == 7

def test_to_upper():
    assert to_upper("cadena") == "CADENA"

def test_to_lower():
    assert to_lower("CADENA") == "CADENA"
