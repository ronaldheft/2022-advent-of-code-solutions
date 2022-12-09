input = open("input.txt", "r")

# Parse the input
lines = input.readlines()
matrix_size = len(lines)

# Iterate left to bottom
max_scenic = -1
for rowIdx, row in enumerate(lines):
    line = row.strip()

    for colIdx, digit in enumerate(line):
        digit = int(digit)

        # Looking left
        score_left = 0
        for c in reversed(range(0, colIdx)):
            option = int(line[c])
            score_left += 1
            if option >= digit: break
        
        # Looking right
        score_right = 0
        for c in range(colIdx+1, matrix_size):
            option = int(line[c])
            score_right += 1
            if option >= digit: break

        # Looking up
        score_up = 0
        for c in reversed(range(0, rowIdx)):
            option = int(lines[c][colIdx])
            score_up += 1
            if option >= digit: break
        
        # Looking down
        score_down = 0
        for c in range(rowIdx+1, matrix_size):
            option = int(lines[c][colIdx])
            score_down += 1
            if option >= digit: break

        score = score_left * score_right * score_up * score_down
        if score > max_scenic:
            max_scenic = score

print("")
print(max_scenic)