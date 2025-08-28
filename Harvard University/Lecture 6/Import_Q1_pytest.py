# We will do that by using the Pytest command
from Question1 import square
def test_Square():
    assert square(2)==4
    assert square(3)==9
    assert square(-2)==4
    assert square(-3)==9
    assert square(0)==0
