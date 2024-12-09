class Layout:
    def __init__(self, id, file_size, free_space) :
        self.id = id
        self.file_size = file_size
        self.free_space = free_space
    
    def print(self):
        print(f"ID: {self.id} BLOCK_SIZE: {self.file_size} FREE_SPACE: {self.free_space} ")

FREE_SPACE = -1
    
def no_gaps(dense_format):
    l = 0

    track = []
    while (l < len(dense_format)):
        if dense_format[l] >= 0:
            l += 1
            while l < len(dense_format) and not dense_format[l] >= 0:
                if dense_format[l] == FREE_SPACE:
                    track.append(FREE_SPACE)
                l += 1

            # Reached end without hitting a digit
            if l < len(dense_format):
                if FREE_SPACE in track and dense_format[l] >= 0 :
                    return False
    return True

def solve(part1):
    f = open('../inputs/day9_test.txt', 'r')
    disk_map = f.readline()
    id_count = 0
    layouts = []
    i = 0

    disk_map = [int(n) for n in disk_map]

    # Gather List of File Info
    while i < len(disk_map) - 2:
        layouts.append(Layout(str(id_count), disk_map[i], disk_map[i+1]))
        id_count += 1
        i += 2
    #print(id_count)
    layouts.append(Layout(str(id_count), disk_map[len(disk_map) - 1], disk_map[len(disk_map) - 2]))


    dense_format = []
    for (i, layout) in enumerate(layouts):
        for _ in range(layout.file_size):
            dense_format.append(int(layout.id))
        
        for _ in range(layout.free_space):
            dense_format.append(FREE_SPACE)


    #print("DENSE", dense_format)

    # Move file blocks from end of disk to leftmost freespace 
    if (part1):

        step = 0
        right = len(dense_format) - 1
        left = 0
        while not no_gaps(dense_format):
            while dense_format[left] != FREE_SPACE:
                left += 1
            
            old = dense_format[right]
            dense_format[right] = FREE_SPACE
            dense_format[left] = old
            right -= 1
            step += 1
        
        #print(dense_format)
        # Checksum
        checksum = 0
        idx = 0
        while dense_format[idx] != FREE_SPACE:
            checksum += int(dense_format[idx]) * idx
            idx += 1
        print("PART 1:" , checksum)
    else:
        print("PART 2: ")






solve(True)
solve(False)

