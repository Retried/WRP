def trojkat_Rysowanie(rozmiar):
    gw = "*"
    i = 1
    while rozmiar >= i:
        print(gw * rozmiar)
        rozmiar -= 1


x = int(input("Podaj wysokość trójkąta: "))

trojkat_Rysowanie(x)
