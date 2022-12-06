input = open("input.txt", "r")

def is_marker(msg):
    if len(msg) >= 4:
        last_four = msg[-4:]
        return len(set(last_four)) == 4
    else:
        return False

for row in input.readlines():
    msg = []
    for i, char in enumerate(row.strip()):
        msg.append(char)
        if is_marker(msg):
            print(i+1)
            break