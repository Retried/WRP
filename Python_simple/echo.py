import sys

terminator = "\n"
rev = False
upp = False

for i, each in enumerate(sys.argv[1:]):
    if each == "-n":
        terminator = ""
    elif each == "-r":
        rev = True
    elif each == "-u":
        upp = True
    else:
        break

args = sys.argv[i+1:]
if rev:
    args = list(reversed(args))

if upp:
    for i, arg in enumerate(args):
        args[i] = arg.lower()
    args[0] = args[0].capitalize()

print(" ".join(args), end=terminator)

lista = ["x", "y", "z"]
print(lista)
print(list(enumerate(lista)))
