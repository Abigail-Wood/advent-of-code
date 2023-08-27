#!/usr/bin/env python3

class File:
    def __init__ (self, name, size):
        self.name = name
        self.size = size

class Directory:
    def __init__ (self, name, parent = None):
        self.name = name
        self.contents = {}
        self.total_size = 0
        if parent:
            self.parent = parent

with open("input.txt", 'r') as f:
    root = Directory('/')
    directories = set([root])
    current_directory = root
    current_directory.parent = root
    for line in list(f):
        line = line.strip().split()
        if line[0] == '$':
            # Interpret the ls and cd commands.
            command = line[1]
            if command == 'ls':
                continue
            elif command == 'cd':
                option = line[2]
                if option in current_directory.contents:
                    current_directory = current_directory.contents[line[2]]
                elif option == '..':
                    current_directory = current_directory.parent
                elif option == '/':
                    current_directory = root
            else:
                print(f"Unrecognised command {command}")
        else:
            # interpret the output
            i0 = line[0]
            if i0 == 'dir':
                dir = Directory(line[1], current_directory)
                current_directory.contents[line[1]] = dir
                directories.add(dir)
            else:
                file_size = int(i0)
                current_directory.contents[line[1]] = File(line[1], file_size)
                d = current_directory
                while True:
                    d.total_size += file_size
                    if d.name == "/":
                        break
                    d = d.parent

# Determine total size of each directory.
# The total size of a directory is the sum of the sizes of the files it contains, directly or indirectly.
# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
print(f"Part 1 answer is: {sum(d.total_size for d in directories if d.total_size <= 100_000)}")

# Total disk space: 70000000; required space: 30000000
# You need to find a directory you can delete that will free up enough space to run the update.
# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. 
# What is the total size of that directory?
total_disk_space = 70000000
required_space = 30000000
total_used_space = root.total_size
unused_space = total_disk_space - total_used_space
deletion_needed = required_space - unused_space

choice = root
for d in directories:
    if (d.total_size >= deletion_needed) & (d.total_size < choice.total_size):
        choice = d

print(f"Part 2 answer is: {choice.total_size}")
