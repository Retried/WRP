class Shape:
    def __init__(self, n=None):
        self.n = n

    def make_n(self, n):
        if n is None:
            n = self.n
        return n

    def draw(self, n=None):
        n = self.make_n(n)
        for i in range(1, n + 1):
            self.draw_line(i, n)

    def scale(self, f):
        self.n *= f


class Triangle(Shape):
    def draw_line(self, i, n):
        print("*" * i)


class Square(Shape):
    def draw_line(self, i, n):
        print("*" * n)


s = Shape(4)
# s.draw()
t = Triangle(4)
t.draw()
print(" ")
k = Square(4)
k.draw()
print(" ")
X = 5
print(X)


def jakas_funkcja():
    global X
    X += 5


jakas_funkcja()
print(X)
print(" ")
q = Square(2)
q.draw()
print(" ")
q.scale(3)
q.draw()
