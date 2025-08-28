# We will do that by using the Pytest command
from Question1 import square
def test_Postive():
    assert square(2)==4
    assert square(3)==9

def test_Negative():    
    assert square(-2)==4
    assert square(-3)==9

def test_Zero():    
    assert square(0)==0
