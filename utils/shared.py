def read_file_lines(path):
    with open(path, encoding="utf-8") as f:
        return f.read().splitlines()

def read_file_integers(path):
    return map(int, read_file_lines(path))