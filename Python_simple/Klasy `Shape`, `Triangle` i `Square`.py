class Shape:
    def draw(self, n):
        raise NotImplementedError('draw')


class Triangle(Shape):
    def draw(self, n):
        for i in range(1, n + 1):
            print("*" * i)
        print()


class Square(Shape):
    def draw(self, n):
        for i in range(1, n + 1):
            print("*" * n)
        print()


s = Shape()
# s.draw(4)
t = Triangle()
t.draw(4)
q = Square()
q.draw(4)
