def piramida(h):
    i = 1
    x = 1
    s = h - 1
    while i <= h:
        print(" " * s + "*" * x)
        x = x + 2
        i += 1
        s -= 1


y = int(input("Podaj wysokość piramidy: "))

piramida(y)
