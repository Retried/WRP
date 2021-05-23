stack = []


def evaluate_plus(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a + b)
    pass


def evaluate_minus(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(b - a)
    pass


def evaluate_multiply(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(a * b)
    pass


def evaluate_divide(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(b / a)
    pass


def evaluate_integer(expr, stack):
    stack.append(int(expr))


operators = {
    "+": evaluate_plus,
    "-": evaluate_minus,
    "*": evaluate_multiply,
    "/": evaluate_divide,
    "p": lambda stack: print(stack[-1])

}


def evaluate_expression(expr, stack):
    for e in expr:
        try:
            evaluate_integer(e, stack)
        except ValueError:
            operators[e](stack)
        '''
        if e == "+":
            evaluate_plus(stack)
        elif e == "-":
            evaluate_minus(stack)
        elif e == "*":
            evaluate_multiply(stack)
        elif e == "/":
            evaluate_divide(stack)
        elif e == "%":
            a = stack.pop()
            b = stack.pop()
            stack.append(b % a)
        elif e == "^":
            a = stack.pop()
            b = stack.pop()
            stack.append(b ** a)
        elif e == "p":
            print(stack[-1])
            print(stack)
        '''
    pass


while True:
    expr = input()
    expr = expr.split()
    done = evaluate_expression(expr, stack)
    if done:
        break
