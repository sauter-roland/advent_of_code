def read_files(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines

def get_joltage(battery: str) -> int:
    battery = battery.strip()
    first, index = 0, 0
    second = 0
    for idx, char in enumerate(battery[:-1]):
        number = int(char)
        if number > first:
            first = number
            index = idx
    for char in battery[index + 1:]:
        number = int(char)
        if number > second:
            second = number
    return 10 * first + second
    
batteries = read_files('./2025/03/data.txt')
total = 0
for battery in batteries:
    total += get_joltage(battery)
print(total)

