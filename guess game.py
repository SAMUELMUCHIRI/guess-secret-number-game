import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess= int(input(f'guess a random number'))
        if guess < random_number:
            print("sorry guess is to low guess again")
        elif guess >random_number:
            print("guess is to high")
    print(f"jackpot you did it ")

guess(80)