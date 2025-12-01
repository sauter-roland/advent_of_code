def read_instructions(file_path: str) -> list[tuple[str, int]]:
    with open(file_path, 'r') as file:
        content = file.read()
    lines = content.splitlines()
    return [(line[0], int(line[1:])) for line in lines if line]

def turn(start: int, direction: str, clicks: int) -> int:
    n = 100
    zeroes = 0
    if direction == 'L':
        new = (start - clicks)
        if new <= 0:
            zeroes += (new // -n) + 1
            if start == 0:
                zeroes -= 1
    elif direction == 'R':
        new = (start + clicks)
        zeroes += new // n
    else:
        raise ValueError("Invalid direction")
    return (zeroes, new % n)

instructions = read_instructions('./2025/01/data.txt')
zeroes = 0
position = 50 
for direction, clicks in instructions:
    new_zeroes, position = turn(position, direction, clicks)
    zeroes += new_zeroes

print(position)
print(f"Times at zero: {zeroes}")

# 5782