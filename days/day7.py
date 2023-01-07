from enum import IntEnum
import re

def calculate(lines, part):
    file_system = FileSystem()
    current_directory = file_system.current_directory
    directories = {current_directory: 0}

    for line in lines:
        match _parse_line(line):
            case ("cd", target):
                current_directory = file_system.change_directory(target)
            case "list":
                pass
            case ("directory", name):
                new_directory = current_directory.add_directory(name, current_directory)
                directories[new_directory] = 0
                # print(f'Added directory {new_directory}')
            case ("file", name, size):
                current_directory.add_file(name, size)
                directory = current_directory
                while directory is not None:
                    if directory in directories:
                        new_size = directories[directory] + size
                        # print(f'New size of directory {directory}: {new_size}')
                        if new_size > 100000:
                            del directories[directory]
                            # print(f'Removing directory {directory}')
                        else:
                            directories[directory] = new_size
                    directory = directory.parent

    return sum([directories[item] for item in list(directories)])

def _parse_line(line):
    if (parsed_instruction := _parse_instruction(line)):
        return parsed_instruction
    if (parsed_item := _parse_item(line)):
        return parsed_item

def _parse_instruction(line):
    if (parsed_instruction_cd := _parse_instruction_cd(line)):
        return parsed_instruction_cd
    if (parsed_instruction_list := _parse_instruction_ls(line)):
        return parsed_instruction_list

def _parse_instruction_cd(line):
    if (parsed := _regex_instruction_cd.match(line)):
        return ("cd", str(parsed.group(1)))

def _parse_instruction_ls(line):
    if _regex_instruction_ls.match(line):
        return "list"

def _parse_item(line):
    if (parsed_item_dir := _parse_item_dir(line)):
        return parsed_item_dir
    if (parsed_item_file := _parse_item_file(line)):
        return parsed_item_file

def _parse_item_dir(line):
    if (parsed_item_dir := _regex_item_dir.match(line)):
        return ("directory", str(parsed_item_dir.group(1)))

def _parse_item_file(line):
    if (parsed_item_file := _regex_item_file.match(line)):
        return ("file", str(parsed_item_file.group(2)), int(parsed_item_file.group(1)))

class Mode(IntEnum):
    COMMAND = 1,
    LIST = 2

class ChangeDirectoryInstruction:
    def __init__(self, target):
        self.target = target

    def __repr__(self):
        return f'ChangeDirectoryInstruction({self.target=})'

class ListInstruction:
    def __init__(self):
        pass

    def __repr__(self):
        return "ListInstruction()"

class FileSystem:
    def __init__(self):
        self._root_directory = Directory("/", None)
        self._current_directory = self.root_directory
    
    @property
    def root_directory(self):
        return self._root_directory

    @property
    def current_directory(self):
        return self._current_directory

    def change_directory(self, target):
        match target:
            case "/":
                self._current_directory = self._root_directory
            case "..":
                parent = self._current_directory.parent
                self._current_directory = parent
            case _:
                if (target_directory := self._current_directory.find_directory(target)):
                    self._current_directory = target_directory
        return self.current_directory

class FileSystemItem:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

class Directory(FileSystemItem):
    def __init__(self, name, parent):
        super().__init__(name)
        self._files = []
        self._directories = {}
        self._parent = parent

    def __repr__(self):
        return f'Directory({self.name=})'

    @property
    def files(self):
        return self._files

    @property
    def directories(self):
        return self._directories

    @property
    def parent(self):
        return self._parent

    def add_file(self, name, size):
        file = File(name, size)
        self._files.append(file)
        return file

    def add_directory(self, name, parent):
        directory = Directory(name, parent)
        self._directories[name] = directory
        return directory

    def find_directory(self, name):
        return self._directories.get(name)

class File(FileSystemItem):
    def __init__(self, name, size):
        super().__init__(name)
        self._size = size

    def __repr__(self):
        return f'File({self.size=}, {self.name=})'

    @property
    def size(self):
        return self._size

_regex_instruction_cd = re.compile(r"^\$\scd\s([/.a-z]+)$")
_regex_instruction_ls = re.compile(r"^\$\sls$")
_regex_item_dir = re.compile(r"^dir\s([a-z]+)$")
_regex_item_file = re.compile(r"^(\d+)\s([a-z\.]+)$")