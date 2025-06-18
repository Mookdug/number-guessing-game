import random

def main():
    print("Welcome to the Number Guessing Game!")
    secret = random.randint(1, 100)
    guesses = 0

    while True:
        try:
            guess = input("Enter your guess (1-100): ").strip()
            if not guess.isdigit():
                print("Please enter a valid number.")
                continue

            guess = int(guess)
            guesses += 1

            if guess < secret:
                print("Too low. Try again.")
            elif guess > secret:
                print("Too high. Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {guesses} tries.")
                break
        except Exception as e:
            print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
