from app import greet, add, mult

def test_greet():
    assert greet("Bob") == "Hello, Bob!"

def test_add():
    assert add(2, 5) == 7

def test_mult():
    assert mult(3, 5) == 15 
    