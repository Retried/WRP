def square_shape(length):
    print("* " * length)
    for _ in range(length - 2):
        print("* " + "  " * (length - 2) + "*")
    print("* " * length)


x = int(input("Podaj wysokość kwadratu: "))

square_shape(x)
