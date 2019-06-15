import random

num = random.randint(0, 10)

print(num)

guessCount = 0

while guessCount < 5:

    guess = input("Take a guess:")
    guess = int(guess)

    guessCount += 1

    if guess < num:
        print("Your guess was too small")
    elif guess > num:
        print("Your guess was too big")
    else:
        print("Well Done !!  You are correct")2
        break


print("You took " + str(guessCount) + " guesses")