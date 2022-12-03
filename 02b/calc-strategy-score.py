SHAPE_VALUES = {'A': 1, 'B': 2, 'C': 3}
RESULT_VALUES = {'X': 0, 'Y': 3, 'Z': 6}

input = open("input.txt", "r")

def value_for_shape(shape):
    return SHAPE_VALUES[shape]

def value_for_result(result):
    return RESULT_VALUES[result]

def response_for_round(opponent_value, result):
    response = 0
    if result == 'X': # Lose
        response = opponent_value - 1
    elif result == 'Y': # Draw
        response = opponent_value
    elif result == 'Z': # Win
        response = opponent_value + 1
    else:
        raise ValueError('Unknown result value: ' + result)
    
    if response < 1:
        return 3
    elif response > 3:
        return 1
    else:
        return response

# Process the strategy guide
match_result = 0
for round in input.readlines():
    opponent = round[0]
    result = round[2]
    opponent_value = value_for_shape(opponent)
    response_value = response_for_round(opponent_value, result)
    result_value = value_for_result(result)
    round_value = response_value + result_value
    match_result += round_value

print(match_result)