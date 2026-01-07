import random

def guess_game():
    secret_number = random.randint(1, 10)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess a number (1-10): "))
            attempts += 1
            
            if guess == secret_number:
                print(f"Correct! You took {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == '__main__':
    guess_game()

# Conceptual Output:
# Guess a number (1-10): 5
# Too low. Try again.
# Guess a number (1-10): 8
# Too high. Try again.
# Guess a number (1-10): 6
# Correct! You took 3 attempts.
