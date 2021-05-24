def simple_decorator(fn):
    def impl(x):
        x += 1
        fn(x)

    return impl


@simple_decorator
def printer(x):
    print(x)


printer(3)
print(printer)
