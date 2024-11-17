import itertools

numbers = []

for numbers in itertools.product("01234567", repeat=5):
    numbers.append(numbers)

print(numbers)