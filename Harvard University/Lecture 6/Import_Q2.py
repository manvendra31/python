from Question2 import squ
import pytest

def test_Postive():
    assert squ(2)==4
    assert squ(3)==9

def test_Negative():    
    assert squ(-2)==4
    assert squ(-3)==9

def test_Zero():    
    assert squ(0)==0

def test_str():
    with pytest.raises(TypeError):
        squ("cat")