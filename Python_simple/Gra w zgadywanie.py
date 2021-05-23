import random

x = random.randint(0, 100)
while True:
    n = int(input("Podaj liczbę: "))
    if x > n:
        print("Za mało!")
    elif x < n:
        print("Za dużo!")
    else:
        print("W sam raz!")
        break
