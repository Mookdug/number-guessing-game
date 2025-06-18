import random

def main():
    print("🎯 Welcome to the Number Guessing Game!")
    secret = random.randint(1, 100)
    guesses = 0

    while True:
        try:
            guess = int(input("Enter your guess (1–100): "))
            guesses += 1

            if guess < secret:
                print("Too low. Try again.")
            elif guess > secret:
                print("Too high. Try again.")
            else:
                print(f"🎉 Correct! You guessed it in {guesses} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
