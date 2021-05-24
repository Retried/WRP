class Basic:
    def __init__(self, field):
        self.field = field

    def __str__(self):
        return "basic {x}".format(x=self.field)

    def print_field(self):
        return print(self.field)

    def __gt__(self, other):
        return self.field > other.field


class X:
    def __init__(self, field):
        self.field = field


def print_field(x):
    return print(x.field)


c = Basic(-5)
b = Basic(10)
x = X("Hello")
print(b)
b.print_field()
Basic.print_field(b)
print_field(x)
Basic.print_field(x)
