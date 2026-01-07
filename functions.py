def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Positional argument
result1 = greet("Alice")

# Keyword argument
result2 = greet(name="Bob", greeting="Hi")

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")

# Expected Output:
# Result 1: Hello, Alice!
# Result 2: Hi, Bob!
