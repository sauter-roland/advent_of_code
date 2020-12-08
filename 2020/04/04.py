from typing import Dict, List
import re

FIELDS = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    #'cid',
]

RE_HCL = re.compile('\#[0-9a-f]{6}')
VALID_ECL = ['amb', 'blue', 'brn', 'gry', 'grn', 'hzl', 'oth']
RE_PID = re.compile('[0-9]{9}')

def parsePassports(filepath):
    with open(filepath) as f:
        passports = f.read().split('\n\n')
    passports = [p.split() for p in passports]
    passport_dicts = [parseToDict(p) for p in passports]

def parseToDict(passport: List[str]):
    pass_dict = {}
    for field in passport:
        field_parsed = field.split(':')
        pass_dict[field_parsed[0]] = field_parsed[1]
    return pass_dict

def checkPresenceOfFields(passport: Dict) -> bool:
    for field in FIELDS:
        if not field in passport.keys():
            return False
    return True

def checkYear(passport: Dict, tag: str, min: int, max: int):
    try:
        year = int(passport['byr'])
    except:
        return False
    return (min <= year <= max)

def checkHgt(passport:Dict):
    height = passport['hgt']
    try:
        number = height[:-2]
    if height.endswith('cm'):
        return (150 <= number <= 193)
    elif height.endswith('in'):
        return (59 <= number <= 76)
    else:
        return False

def checkHcl(passport:Dict):
    color = passport('hcl')
    if not len(color) == 7:
        return False
    if not RE_HCL.match(color):
        return False
    return True
    
def checkEcl(passport: Dict):
    color = passport['ecl']
    if color in VALID_ECL:
        return True
    else:
        return False

def checkPid(passport: Dict):
    if RE_PID.match(passport['pid']):
        return True
    else:
        return False

def checkPassport():
    pass

passports = parsePassports('input_04.txt')
validity = [check_validity(p) for p in passports]
print(sum(validity))