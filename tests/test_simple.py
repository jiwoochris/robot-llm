# /tests/test.py

# Here is the function we're going to test
def add(a, b):
    return a + b


# Here are our pytest tests for the add function
def test_add():
    assert add(1, 1) == 2
    assert add(-1, -1) == -2
    assert add(0, 5) == 5