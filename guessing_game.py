import random

def guessing_game():
    number = random.randint(1, 10)

    while True:
        try:
            guess = int(input("Guess a number between 1 and 10: "))

            if guess < 1 or guess > 10:
                print("Please enter a number between 1 and 10.")
                continue

            if guess == number:
                print("Yeah, you guessed it!")
                break
            else:
                print("Try again!")

        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        guessing_game()

        again = input("Do you want to play again? (y/n): ")

        if again.lower() != "y":
            print("Goodbye!")
            break


main()