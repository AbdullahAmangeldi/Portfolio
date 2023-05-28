import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("Try to guess a number! It's between 1 and 100.")

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("The number is higher than that!")
        elif guess > secret_number:
            print("The number is lower than that!")
        else:
            print(f"Congratulations! Number of attempts:{attempts}")
            break

guess_number()
