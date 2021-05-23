n = 15

for i in range(1, n + 1):
    fizz_buzz = []
    if i % 3 == 0:
        fizz_buzz.append("Fizz")
    if i % 5 == 0:
        fizz_buzz.append("Buzz")
    if fizz_buzz:
        print(i, "".join(fizz_buzz))
