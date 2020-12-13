# URL: https://adventofcode.com/2020/day/6

input_values = '''abc

a
b
c

ab
ac

a
a
a
a

b'''.split('\n')

puzzle_values = [line.strip() for line in open("input.txt", "r")]


def get_sum_answers_anyone(input_values):
    d = set()
    sum = 0
    for line in input_values:
        if line == '':
            sum += len(d)
            d = set()
            continue
        for c in line:
            d.add(c)
    sum += len(d)
    return sum


def get_sum_answers_everyone(input_values):
    d = {}
    sum = 0
    group_len = 0
    input_values.append('')
    for line in input_values:
        if line == '':
            for[k, v] in d.items():
                if v == group_len:
                    sum += 1
            d = {}
            group_len = 0
            continue
        group_len += 1
        for c in line:
            if d.get(c,None) != None:
                d[c] += 1
            else:
                d[c] = 1
    return sum


r = get_sum_answers_anyone(input_values)
print(r)

r = get_sum_answers_anyone(puzzle_values)
print(r)


r = get_sum_answers_everyone(input_values)
print(r)

r = get_sum_answers_everyone(puzzle_values)
print(r)
