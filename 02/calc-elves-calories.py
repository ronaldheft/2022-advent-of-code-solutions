input = open("input.txt", "r")

# Track the results
current_elf = 0
elf_calorie_list = []

# Process the calorie list
for line in input.readlines():
    is_new_elf = len(line.strip()) == 0
    
    if is_new_elf:
        elf_calorie_list.append(current_elf)
        # Reset the current elf to zero
        current_elf = 0
    else:
        # Add the line's calories to the current elf
        current_elf += int(line)

# Sort the list of calories
elf_calorie_list.sort(reverse=True)

# Print the total of top 3 calories
elf_top_3 = elf_calorie_list[0:3]
elf_top_3_calories = sum(elf_top_3)
print(elf_top_3_calories)