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
count = 0
while count < counter:
    count += 1
    break

# Taking a Guess Input
guess = int(input("Guess a number: "))

# Condition Testing
if x == guess:
    print(f"Congratulations!  You guessed correctly in", count, "tries!")
elif x > guess:
    print("Your guess was low!")
elif x < guess:
    print("Your guess was high!")

# If guesses exceeds the allowed amount
if count >= counter:
    print(f"Guesses tried:", count)
    print("Better luck next time!")
