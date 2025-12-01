with open('2025/01/data.txt', 'r') as file:
    content = file.read()
lines = content.splitlines()
instructions = [(line[0], int(line[1:])) for line in lines if line]

for instruction in instructions:
    assert isinstance(instruction[0], str)
    assert isinstance(instruction[1], int)

def turn(start: int, direction: str, clicks: int) -> int:
    n = 100
    if direction == 'L':
        return (start - clicks) % n
    elif direction == 'R':
        return (start + clicks) % n
    else:
        raise ValueError("Invalid direction")

zeroes = 0
position = 50 
for direction, clicks in instructions:
    position = turn(position, direction, clicks)
    if position == 0:
        zeroes += 1

print(position)
print(f"Times at zero: {zeroes}")