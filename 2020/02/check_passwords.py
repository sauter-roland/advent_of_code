def parse_str(password_str):
    password_parts = password_str.split(': ')
    letter_parts = password_parts[0]
    password = password_parts[1]
    letter_parts = letter_parts.split(' ')
    letter = letter_parts[1]
    bounds = letter_parts[0]
    bounds = bounds.split('-')
    return password, letter, int(bounds[0]), int(bounds[1])

def check_password_first(password_str):
    password, letter, lower, upper = parse_str(password_str)
    occurences = password.count(letter)
    if (occurences > upper) or (occurences < lower):
        return False
    return True

def check_password_second(password_str):
    password, letter, lower, upper = parse_str(password_str)
    lower -= 1; upper -= 1 # Python is zero indexed
    if (password[lower] == password[upper] == letter):
        return False
    elif (password[lower] == letter) or (password[upper] == letter):
        return True
    return False

def check_list(filepath):
    with open(filepath, 'r') as f:
        passwords = f.readlines()
    results = [check_password_second(p) for p in passwords]
    corrects = sum(results)
    return corrects

print(check_list('input_01.txt'))