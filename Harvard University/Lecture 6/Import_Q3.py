from Question3 import hello

def test_defult():
    assert hello("")=="hello, world"

def test_argument():
    assert hello("Manvendra")=="Hello, Manvendra"