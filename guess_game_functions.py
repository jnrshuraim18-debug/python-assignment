import random

def generate_secret_number():
    """Generate a random secret number between 1 and 10"""
    return random.randint(1, 10)

def get_user_guess():
    """Prompt the user for a valid number"""
    while True:
        guess = input("Take a guess: ")
        if guess.isdigit():
            return int(guess)
        else:
            print("Please enter a number.")

def check_guess(guess, secret_number):
    """Check if the guess is too low, too high, or correct"""
    if guess < secret_number:
        print("Too low! Try again.")
        return False
    elif guess > secret_number:
        print("Too high! Try again.")
        return False
    else:
        print("Woww Correct! You guessed the number!")
        return True

def play_game():
    """Main game loop"""
    secret_number = generate_secret_number()
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        guess = get_user_guess()
        if check_guess(guess, secret_number):
            break

# Run the game
if __name__ == "__main__":
    play_game()
