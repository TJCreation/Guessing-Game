import random
import math


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
while count <= counter:
    guess = int(input("Guess a number: "))
    if x == guess:
        print(f"Congratulations!  You guessed correctly in", count, "tries!")
        break
    elif x > guess:
        print("Your guess was low!")
        count += 1
        print(f"You are on guess number:", count,)
    elif x < guess:
        print("Your guess was high!")
        count += 1
        print(f"You are on guess number:", count, )


# If guesses exceeds the allowed amount
if count > counter:
    print(f"Guesses tried:", count)
    print("Better luck next time!")
