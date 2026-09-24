from app import add, divide

def test_add():
    assert add(2, 3) == 6
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5
