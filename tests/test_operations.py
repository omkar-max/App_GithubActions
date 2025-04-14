from src.math_operations import add, subtract
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-1, -1) == -2
    assert add(1.5, 2.5) == 4.0
    assert add(1, -1) == 0  
    assert add(1000000, 2000000) == 3000000
    assert add(0.1, 0.2) == 0.30000000000000004 # Floating point precision issue
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(0, 0) == 0
    assert subtract(-1, 0) == -1
    assert subtract(2, 3) == -1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0  
    assert subtract(-1, -1) == 0
