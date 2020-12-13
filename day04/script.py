import re
input_values = [
    'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
    'byr:1937 iyr:2017 cid:147 hgt:183cm',
    '',
    'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
    'hcl:#cfa07d byr:1929',
    '',
    'hcl:#ae17e1 iyr:2013',
    'eyr:2024',
    'ecl:brn pid:760753108 byr:1931',
    'hgt:179cm',
    '',
    'hcl:#cfa07d eyr:2025 pid:166559648',
    'iyr:2011 ecl:brn hgt:59in',
]

puzzle_values = [line.strip() for line in open("input.txt", "r")]


def has_valid_keys(passport):
    # print(passport)
    if len(passport) < 7:
        return False
    if len(passport) == 7:
        return not 'cid' in passport
    return True

def check_height(hgt):
    m = re.search(r"^(\d+)in$", hgt)
    if m and 59<=int(m.groups()[0]) <=76:
        return True
    m = re.search(r"^(\d+)cm$", hgt)
    if m and 150<=int(m.groups()[0]) <=193:
        return True
    return False

def has_valid_values(passport):
    return (1920 <= int(passport['byr']) <= 2002) and \
        (2010 <= int(passport['iyr']) <= 2020) and \
        (2020 <= int(passport['eyr']) <= 2030) and \
        check_height(passport['hgt']) and \
        (re.search(r"^#[0-9a-f]{6}$", passport['hcl'])) and \
        passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] and \
        (re.search(r"^\d{9}$", passport['pid']))


def count_passports(input_values):
    count = 0
    passport = {}
    for line in input_values:
        if line == '':
            if has_valid_keys(passport.keys()) and has_valid_values(passport):
                # print(passport)
                count += 1
            else:
                # print(passport)
                pass
            passport = {}
            continue
        for value in line.split(' '):
            [k, v] = value.split(':')
            passport[k] = v

    if has_valid_keys(passport.keys()) and has_valid_values(passport):
        count += 1
        print(passport)
    else:
        # print(passport)
        pass
    return count


res = count_passports(input_values)
print(res)
res = count_passports(puzzle_values)
print(res)
