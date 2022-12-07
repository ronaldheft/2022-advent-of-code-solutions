input = open("input.txt", "r")

calculated_size = 0

# Our base classes
class FileSystem:
    def get_size(self):
        raise NotImplementedError

class Dir(FileSystem):
    def __init__(self, name, parent = None):
        super().__init__()
        self.name = name
        self.contents = []
        self.parent = parent
    
    def get_size(self):
        total_file_size = 0
        total_folder_size = 0
        
        for item in self.contents:
            if isinstance(item, Dir):
                total_folder_size += item.get_size()
            elif isinstance(item, File):
                total_file_size += item.get_size()
        
        total_size = total_file_size + total_folder_size
        print(self.name + ": " + str(total_size))

        if total_size <= 100000:
            global calculated_size
            calculated_size += total_size

        return total_size


class File(FileSystem):
    def __init__(self, name, size):
        super().__init__()
        self.name = name.strip()
        self.size = int(size.strip())
    
    def get_size(self):
        return self.size

# Initialize the directory structure
base_dir = Dir("/")
pointer = base_dir
print(pointer)

# Helper methods
def is_directory_change(line):
    return line.startswith("$ cd")

def handle_dir_change(line):
    global pointer
    global base_dir
    name = line[5:]
    
    if name == "..":
        pointer = pointer.parent
    elif name == "/":
        pointer = base_dir
    else:
        folder = Dir(name, parent = pointer)
        pointer.contents.append(folder)
        pointer = folder

def is_file_list(line):
    return not line.startswith("$") and not line.startswith("dir")

def handle_file(line):
    output = line.strip().split(" ")
    file = File(name=output[1], size=output[0])
    pointer.contents.append(file)

# Parse the input
for row in input.readlines():
    line = row.strip()
    
    if is_directory_change(line):
        handle_dir_change(line)
    elif is_file_list(line):
        handle_file(line)
    else:
        print("unknown: " + line)

# Debug the output
print(base_dir.get_size())
print("Answer: " + str(calculated_size))