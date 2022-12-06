import re

input = open("input.txt", "r")

# Use a dictionary for our stacks to bypass zero-based arrays
stacks = {}

def parse_stack(stack_row):
    # Assume a stack row has at least one "[" in the line
    if "[" not in stack_row:
        return False
    
    row_length = len(stack_row)
    stack_counter = 1 # Start at the first stack
    index = 1 # Start at the first letter, which is always at index 1
    while index != -1: # Terminate the while loop with a -1
        item = stack_row[index].strip()
        
        # Create or update a stack with the item
        if item:
            if stack_counter not in stacks:
                stacks.update({stack_counter: [item]})
            else:
                stacks[stack_counter].append(item)
        
        # Always increase the stack counter
        stack_counter += 1

        # The next item +4 away
        index += 4

        # Handle the end of the row by terminating our while loop
        if index > row_length:
            index = -1

    return True

def process_move(move):
    move_match = re.search(r"(?:move )(?P<count>\d+)(?: from )(?P<from>\d+)(?: to )(?P<to>\d+)", move)
    items = []
    for x in range(int(move_match.group("count"))):
        # Possible error if stack is empty, may need to handle
        items.append(stacks[int(move_match.group("from"))].pop(0))
    for item in reversed(items):
        stacks[int(move_match.group("to"))].insert(0, item)


is_parsing_stacks = True
is_parsing_moves = False
result = ""
for row in input.readlines():
    # Handle a blank row
    if len(row.strip()) == 0:
        continue

    # Parse stack rows until empty
    if is_parsing_stacks:
        is_stack_row = parse_stack(row)
        if is_stack_row is False:
            is_parsing_stacks = False
            is_parsing_moves = True
            continue
    
    # Parse move rows until done
    if is_parsing_moves:
        process_move(row)

# Get the top item in each stack
for key in sorted(stacks.keys()):
    # This removes the top item, which is okay for our use case
    result += stacks[key].pop(0)

print(result)