def read_file_content(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def read_file_lines(path):
    with open(path, encoding="utf-8") as f:
        return f.read().splitlines()

def read_file_integers(path):
    return map(int, read_file_lines(path))

def sign(value: int) -> int:
    return (value > 0) - (value < 0)