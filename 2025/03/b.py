def read_files(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines

def get_joltage(battery: str, n_batteries: int) -> int:
    battery = battery.strip()
    picked = []
    idx = 0
    # pick the largest possible digit while leaving just enough chars for the remainder
    while len(picked) < n_batteries:
        remaining = n_batteries - len(picked)
        go_until = len(battery) - remaining + 1
        number, new_idx = get_max_and_idx_in_range(battery, idx, go_until)
        picked.append(number)
        idx = new_idx
    return ''.join(str(d) for d in picked)

def get_max_and_idx_in_range(battery: str, idx: int, go_until: int) -> tuple[int, int]:
    current_max = -1
    max_idx = -1
    for current_idx, char in enumerate(battery[idx:go_until]):
        number = int(char)
        if number > current_max:
            current_max = number
            max_idx = current_idx
    # need to add 1 to actually move forward
    return current_max, max_idx + idx + 1

batteries = read_files('./2025/03/data.txt')
total = 0
for battery in batteries:
    total += int(get_joltage(battery, 12))
print(total)
