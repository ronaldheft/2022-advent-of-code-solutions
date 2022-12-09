input = open("input.txt", "r")

# Parse the input
lines = input.readlines()
matrix_size = len(lines)
matrix = [[False for col in range(matrix_size)] for row in range(matrix_size)]

# Iterate left to bottom
max_row = [-1 for row in range(matrix_size)]
for rowIdx, row in enumerate(lines):
    line = row.strip()
    
    max_col = -1
    for colIdx, digit in enumerate(line):
        digit = int(digit)

        # From the left
        if colIdx == 0:
            matrix[rowIdx][colIdx] = True
        elif digit > int(line[colIdx-1]) and digit > max_col:
            matrix[rowIdx][colIdx] = True
        
        # From the top
        if rowIdx == 0:
            matrix[rowIdx][colIdx] = True
        elif digit > int(lines[rowIdx-1][colIdx]) and digit > max_row[colIdx]:
            matrix[rowIdx][colIdx] = True
        
        if digit > max_col:
            max_col = digit
        if digit > max_row[colIdx]:
            max_row[colIdx] = digit

# Iterate right to top
lines = list(reversed(lines))
max_row = [-1 for row in range(matrix_size)]
for rowIdx, row in enumerate(lines):
    line = row.strip()
    
    line = list(reversed(line))
    max_col = -1
    for colIdx, digit in enumerate(line):
        digit = int(digit)

        # From the right
        if colIdx == 0:
            matrix[matrix_size-rowIdx-1][matrix_size-colIdx-1] = True
        elif digit > int(line[colIdx-1]) and digit > max_col:
            matrix[matrix_size-rowIdx-1][matrix_size-colIdx-1] = True
        
        # From the bottom
        if rowIdx == 0:
            matrix[matrix_size-rowIdx-1][matrix_size-colIdx-1] = True
        elif digit > int(lines[rowIdx-1][matrix_size-colIdx-1]) and digit > max_row[colIdx]:
            matrix[matrix_size-rowIdx-1][matrix_size-colIdx-1] = True
        
        if digit > max_col:
            max_col = digit
        if digit > max_row[colIdx]:
            max_row[colIdx] = digit

visible_count = 0
for row in matrix:
    for cell in row:
        if cell:
            visible_count += 1
            print("T", end="")
        else:
            print("F", end="")
    print("")

print(visible_count)