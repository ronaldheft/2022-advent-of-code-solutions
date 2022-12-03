SHAPE_VALUES = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

input = open("input.txt", "r")

def value_for_shape(shape):
    return SHAPE_VALUES[shape]

def result_for_round(opponent_value, response_value):
    if opponent_value == response_value:
        return 3 # Draw
    elif response_value == (opponent_value + 1) or (response_value == 1 and opponent_value == 3):
        return 6 # Win
    else:
        return 0 # Loss

# Process the strategy guide
match_result = 0
for round in input.readlines():
    opponent = round[0]
    response = round[2]
    opponent_value = value_for_shape(opponent)
    response_value = value_for_shape(response)
    result = result_for_round(opponent_value, response_value)
    round_value = response_value + result
    match_result += round_value

print(match_result)