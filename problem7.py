sizes = []


class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.subfolders = []
        self.files = dict()
        self.parent = parent


def main():
    with open("sample7.txt") as file:
        commands = file.readlines()
    root = Folder(name='/', parent=None)
    current_folder = None
    for command in commands:
        if command[0] == '$':
            if command[2:4] == 'cd':
                if command[5:7] == '..':
                    current_folder = current_folder.parent
                else:
                    folder_name = command[5:].strip()
                    if folder_name == '/':
                        current_folder = root
                    else:
                        for folder in current_folder.subfolders:
                            if folder.name == folder_name:
                                current_folder = folder
        else:
            if command[:3] == 'dir':
                folder_name = command[4:].strip()
                current_folder.subfolders.append(Folder(name=folder_name, parent=current_folder))
            else:
                size, name = command.strip().split(" ")
                size = int(size)
                current_folder.files[name] = size

    sizes = get_size(root)
    large = []
    '''
    PART ONE
    small = 0
    for entry in sizes:
        if entry <= 100000:
            small += entry
    print(small)
    '''
    free_space = 70000000 - dir_size(root)
    required_space = 30000000 - free_space
    for entry in sizes:
        if entry >= required_space:
            large.append(entry)
    print(min(large))
    display_structure(root)


def get_size(folder):
    global sizes
    sizes.append(dir_size(folder))
    for subfolder in folder.subfolders:
        get_size(subfolder)
    return sizes


def find(root, name):
    for folder in root.subfolders:
        if folder.name == name:
            return True
    return False


def get_depth(folder: Folder):
    level = 0
    p = folder.parent
    while p:
        level += 1
        p = p.parent
    return level


def dir_size(folder: Folder):
    total_size = 0
    for entry in folder.files:
        total_size += folder.files[entry]
    for subfolder in folder.subfolders:
        total_size += dir_size(subfolder)
    return total_size


def display_structure(folder: Folder):
    depth = "--" * get_depth(folder)
    print(f"{depth} DIR: {folder.name}")
    for entry in folder.files:
        print(f"{depth} {entry}, {folder.files[entry]}")
    for subfolder in folder.subfolders:
        display_structure(subfolder)


if __name__ == "__main__":
    main()
