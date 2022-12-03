import numpy as np

input = open("input.txt", "r")

def value_for_char(char):
    value = ord(char)
    if value >= 97:
        # Lower case
        return value - 96
    else:
        # Upper case
        return value - 65 + 27

result = 0
for compartment in input.readlines():
    items = list(compartment.strip())
    a = items[:len(items)//2]
    b = items[len(items)//2:]
    intersect = np.intersect1d(a, b)
    duplicate_item = intersect[0]
    result += value_for_char(char = duplicate_item)

print(result)