def greeter(greeting):
    def impl(who):
        print(greeting + who)

    return impl


hello = greeter("Siema")
hello("Ala")
hello("Kot")

greeter("Hello")("World")
