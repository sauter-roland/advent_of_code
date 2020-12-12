def parse(input_file):
    with open(input_file, 'r') as f:
        return f.read().split('\n\n')

def clean_input(answers):
    return [a.replace('\n', '') for a in answers]

def get_uniques(answers):
    return [set(a) for a in answers]

def get_unique_count(answers):
    return [len(a) for a in answers]

def get_agreeing(answers):
    agreeing_total = 0
    for answer in answers:
        n = answer.count('\n') + 1
        count = {}
        for entry in answer.replace('\n', ''):
            try:
                count[entry] += 1
            except KeyError:
                count[entry] = 1
        agreeing = [letter for letter, number in count.items() if number == n]
        agreeing_total += len(agreeing)
    return agreeing_total

answers = parse('input_06.txt')
print(get_agreeing(answers))