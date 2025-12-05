from re import compile

def read_ranges(data_file: str) -> list[tuple[int, int]]:
    with open(data_file, 'r') as f:
        content = f.read().split(',')
    ranges = [tuple(map(int, r.split('-'))) for r in content]
    return ranges

ranges = read_ranges('./2025/02/data.txt')
total = 0

def is_fake(number: int) -> bool:
    identifier = str(number)
    reg = compile(r'^(\d{1,})\1$')
    return reg.match(identifier) is not None

def get_invalids(numbers: tuple[int, int]) -> list[int]:
    invalids = []
    start, end = numbers
    for num in range(start, end + 1):
        if is_fake(num):
            invalids.append(num)
    return invalids

for start, end in ranges:
    for num in range(start, end + 1):
        if is_fake(num):
            total += num
print(total)
