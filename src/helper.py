
def read_file_to_list(filename):
    f = open(filename, 'r')
    lines = []

    for line in f:
        lines.append(line.strip())
    
    return lines

def read_file_to_string(filename):
    f = open(filename, 'r')
    s = ""

    for line in f:
        s += (line.strip())

    return s