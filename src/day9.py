class BlockFile:
    def __init__(self, id, size, free_space) :
        self.id = id
        self.size = size
        self.free_space = free_space
    
    def print(self):
        print(f"ID: {self.id} BLOCK_SIZE: {self.size} FREE_SPACE: {self.free_space} ")

    
def no_gaps(block_str):
    l = 0

    track = []
    while (l < len(block_str)):
        if block_str[l].isdigit():
            l += 1
            while l < len(block_str) and not block_str[l].isdigit():
                if block_str[l] == ".":
                    track.append(".")
                l += 1

            # Reached end without hitting a digit
            if l < len(block_str):
                if "." in track and block_str[l].isdigit() :
                    return False
    return True

def solve():
    f = open('../inputs/day9.txt', 'r')
    disk_map = f.readline()
    print(disk_map)
    id_count = 0
    block_files = []
    i = 0

    # Gather List of File Info
    while i < len(disk_map) - 2:
        block_files.append(BlockFile(str(id_count), disk_map[i], disk_map[i+1]))
        id_count += 1
        i += 2
    print(id_count)
    block_files.append(BlockFile(str(id_count), disk_map[len(disk_map) - 1], disk_map[len(disk_map) - 2]))


    # Debugging
    block_str = ""
    for (i, block) in enumerate(block_files):
        block_str += (block.id * int(block.size))
        if (i != len(block_files) - 1):
            block_str += ("." * int(block.free_space))
        block.print()

    #print(block_str)
    block_str = list(block_str)
    #print(block_str)

    # Move file blocks from end of disk to leftmost freespace 
    step = 0
    right = len(block_str) - 1
    left = 0
    while not no_gaps(block_str):
        while block_str[left] != '.':
            left += 1
        
        old = block_str[right]
        block_str[right] = '.'
        block_str[left] = old
        right -= 1
        step += 1
    
    print(block_str)
    # Checksum
    checksum = 0
    idx = 0
    while block_str[idx] != '.':
        checksum += int(block_str[idx]) * idx
        idx += 1
    print(checksum)






solve()