def safe_division():
    try:
        # Note: input() is interactive, so we'll simulate the logic
        # val = 10 / int(input("Enter divisor: "))
        
        # Scenario 1: ZeroDivisionError (if input was '0')
        # val = 10 / 0 
        
        # Scenario 2: ValueError (if input was 'hello')
        # val = 10 / int('hello')
        
        # Scenario 3: Success
        val = 10 / 2
        print(f"Result: {val}")

    except ValueError:
        print("Invalid input! Enter an integer.")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    finally:
        print("Execution complete.")

# safe_division()

# Expected Output (Scenario 1: Input '0'):
# Cannot divide by zero!
# Execution complete.

# Expected Output (Scenario 2: Input 'hello'):
# Invalid input! Enter an integer.
# Execution complete.

# Expected Output (Scenario 3: Success):
# Result: 5.0
# Execution complete.
