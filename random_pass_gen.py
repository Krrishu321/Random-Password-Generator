

import random

import string


print(" Welcome, Random Password Generator")


def random_my_function():

    maximum=int(input("Maximum Number of Password You Want:-"))
    small=string.ascii_lowercase
    big=string.ascii_uppercase
    number=string.digits
    symbol=string.punctuation
    total=big+small+symbol+number
    generator=random.sample(total,maximum)

    Password = "   ".join(generator)
    print(Password)
    random_my_function()
random_my_function()
    