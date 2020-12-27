import random

random=random.randint(1,10)

guess=int(input("enter the number from 1 to 10:"))

while True:
    if guess <random:
        print("Your guess is low:")
        guess=int(input("Try again:"))

    elif guess >random:
        print("Your guess is high:")
        guess=int(input("Try again:"))

    else:
        print("Your guess is correct:")
        break

print("----------------------------")
