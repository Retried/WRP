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
