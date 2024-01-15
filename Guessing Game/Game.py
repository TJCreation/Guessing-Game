import random
import math

# Taking Inputs
lower = int(input("Enter Low Number: "))
upper = int(input("Enter High Number: "))

# Generating Random Number Between Lower and Upper
x = random.randint(lower, upper)
print(f"You have", round(math.log(upper - lower + 1, 2)), "chances to guess the number!")

# Counting Number of Guesses
count = 0
while count < math.log(upper - lower + 1, 2):
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
if count >= math.log(upper - lower + 1, 2):
    print(f"Guesses tried:", count)
    print("Better luck next time!")
