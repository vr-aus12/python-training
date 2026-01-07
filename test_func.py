# Requires func.py in the same directory
def add(a, b):
    # This is a placeholder for the actual function in func.py
    # In a real setup, you would import it: from .func import add
    return a + b 

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

# Expected Output (when running 'pytest test_func.py'):
# 1 passed in 0.01s
