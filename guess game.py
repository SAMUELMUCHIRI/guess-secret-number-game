import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess= int(input(f'guess a random number'))
        print(guess)
guess(20)