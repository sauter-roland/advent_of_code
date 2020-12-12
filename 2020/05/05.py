test = 'BFFFBBFRRR'
up = ['R', 'B']
down = ['F', 'L']

def get_id(partitions):
    inv = partitions[::-1]
    pos = 0
    for i in range(len(test)):
        char = inv[i] # going from the left
        if char in up:
            pos += 2 ** i 
    return pos

def parse_partitions(input_file):
    with open(input_file, 'r') as f:
        return f.read().split('\n')

def find_missing(ids):
    ids = sorted(ids)
    last = ids[0]
    for i in ids[1:]:
        if i - last > 1:
            return i - 1
        last = i

ids = [get_id(p) for p in parse_partitions('input_05.txt')]
print(find_missing(ids))