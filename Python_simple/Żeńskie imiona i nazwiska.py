from Tuple import *
from Zbiór import *
from Funkcja import *

people = []

for n in names:
    for s in surnames:
        if n[-1] == 'a' and looks_like_polish_surname(s):
            s = s[:-1] + 'a'
        people.append((n, s,))
        print(n, s)
