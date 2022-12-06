input = open("input.txt", "r")

def is_marker(msg):
    if len(msg) >= 14:
        last_fourteen = msg[-14:]
        return len(set(last_fourteen)) == 14
    else:
        return False

for row in input.readlines():
    msg = []
    for i, char in enumerate(row.strip()):
        msg.append(char)
        if is_marker(msg):
            print(i+1)
            break