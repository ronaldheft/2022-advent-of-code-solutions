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
group = []
for compartment in input.readlines():    
    group.append(list(compartment.strip()))

    if len(group) == 3:
        # Not an ideal algorithm, requires a refactor
        intersect_ab = np.intersect1d(group[0], group[1])
        intersect_bc = np.intersect1d(group[1], group[2])
        intersect_abc = np.intersect1d(intersect_ab, intersect_bc)
        duplicate_item = intersect_abc[0]
        result += value_for_char(char = duplicate_item)
        group.clear()

print(result)