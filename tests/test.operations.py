from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(4,3)==7

def test_sub():
    assert sub(3,2)==1
    assert sub(4,1)==3
    assert sub(2,3)==-1

