input = open("input.txt", "r")

def assignments_for_row(assignment_row):
    return assignment_row.strip().split(",")

# This assumes assignment is always: LOWER-UPPER
def values_for_assignment(assignment):
    return assignment.split("-")

def range_overlaps_range(range_a, range_b):
    range_one_overlap = int(range_a[1]) - int(range_b[0])
    range_two_overlap = int(range_a[0]) - int(range_b[1])

    both_positive = range_one_overlap > 0 and range_two_overlap > 0
    both_negative = range_one_overlap < 0 and range_two_overlap < 0
    return (both_positive or both_negative) == False

result = 0
for assignment_row in input.readlines():    
    assignments = assignments_for_row(assignment_row)

    # Determine the range size for each assignment
    assignment_a_values = values_for_assignment(assignments[0])
    assignment_b_values = values_for_assignment(assignments[1])
    
    if range_overlaps_range(assignment_a_values, assignment_b_values):
        result += 1

print(result)