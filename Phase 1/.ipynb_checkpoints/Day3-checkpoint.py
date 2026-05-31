import random

correct = random.randint(1, 100)
attemps = 0

guess = int(input("Guess a number between 1 and 100: "))

while guess != correct:
    attemps += 1
    if guess < correct:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 100: "))

print(f"Congratulations! You guessed the number in {attemps} attempts.")