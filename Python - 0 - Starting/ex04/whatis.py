import sys


def even_or_odd(num):
    if num % 2 == 0:
        return "I'm Even"
    else:
        return "I'm Odd"


if len(sys.argv) == 1:
    sys.exit()
if len(sys.argv) > 2:
    raise AssertionError("More than one argument provided")

try:
    number = int(sys.argv[1])
except ValueError:
    raise AssertionError("Argument is not an integer")
    sys.exit()

result = even_or_odd(number)
print(result)
