input = open("input.txt", "r")

# Track the results
current_elf = 0
max_elf = 0

# Process the calorie list
for line in input.readlines():
    is_new_elf = len(line.strip()) == 0
    
    if is_new_elf:
        if current_elf > max_elf:
            max_elf = current_elf
        
        # Reset the current elf to zero
        current_elf = 0
    else:
        # Add the line's calories to the current elf
        current_elf += int(line)

# Print the most calories
print(max_elf)