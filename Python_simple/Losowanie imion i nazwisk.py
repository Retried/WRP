import random
from Tuple import *
from Zbiór import *
from Funkcja import *


def create_a_person(create_name, create_surname):
    x = random.randint(0, len(create_name) - 1)
    random_name = create_name[x]
    x = random.randint(0, len(create_surname) - 1)
    random_surname = create_surname[x]
    if random_name[-1] == 'a' and looks_like_polish_surname(random_surname):
        random_surname = random_surname[:-1] + 'a'
    return "{} {}".format(random_name, random_surname)


print(create_a_person(names, surnames))
