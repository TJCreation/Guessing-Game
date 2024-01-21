import random
import math


def game():
    # Taking Inputs
    lower = int(input("Enter Low Number: "))
    upper = int(input("Enter High Number: "))

    # Creating "counter" Variable
    counter = math.log(upper - lower + 1, 2)

    # Generating Random Number Between Lower and Upper
    x = random.randint(lower, upper)
    print(f"You have", round(counter), "chances to guess the number!")

    # Counting Number of Guesses
    count = 1

    # Taking a Guess Input and Testing the Condition
    while count < counter:
        guess = int(input("Guess a number: "))
        if x == guess:
            print(f"Congratulations!  You guessed correctly in", count, "tries!")
            break
        elif x > guess:
            print("Your guess was low!")
            count += 1
            print(f"You are on guess number:", count, )
        elif x < guess:
            print("Your guess was high!")
            count += 1
            print(f"You are on guess number:", count, )

    # The Final Guess
    while count > counter:
        print("This is your final guess!")
        guess = int(input("Guess a number: "))
        if x == guess:
            print(f"Congratulations!  You guessed correctly in", count, "tries!")
            break
        elif x > guess:
            print("Your guess was low!")
            print("Better Luck Next Time!")
            break
        elif x < guess:
            print("Your guess was high!")
            print("Better Luck Next Time!")
            break


# Allowing Repeated Gameplay
def game_play():
    while True:
        game()
        answer = input("Do you want to play again? Y/N: ")
        if answer == 'N' or 'n':
            print("Thanks For Playing!")
            break


game_play()
