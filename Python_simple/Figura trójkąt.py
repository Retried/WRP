def trojkat_Rysowanie(rozmiar):
    gw = "*"
    i = 1
    while i <= rozmiar:
        print(gw * i)
        i += 1


x = int(input("Podaj wysokość trójkąta: "))

trojkat_Rysowanie(x)
