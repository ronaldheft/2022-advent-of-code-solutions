input = open("input.txt", "r")

directories = []

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
        directories.append(total_size)

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

file_system_size = 70000000
file_system_used = base_dir.get_size()
print("File System Used: " + str(file_system_used))

free_space = file_system_size - file_system_used
print("Free Space: " + str(free_space))

min_free_space = 30000000
min_to_delete = min_free_space - free_space
print("Min to Delete: " + str(min_to_delete))

for dir in sorted(directories):
    if dir >= min_to_delete:
        print(dir)
        break