# URL: https://adventofcode.com/2020/day/5
input_values = [
    'FBFBBFFRLR',
    'BFFFBBFRRR',
    'FFFBBBFRRR',
    'BBFFBBFRLL',
]

puzzle_values = [line.strip() for line in open("input.txt", "r")]

def get_row(s):
    suma = 0
    s = s[::-1]
    for l in range(len(s)):
        suma += (1 if s[l] == 'B' else 0) * (2 ** l)
    print(f'row {suma}')
    return suma

def get_column(s):
    suma = 0
    s = s[::-1]
    for l in range(len(s)):
        suma += (1 if s[l] == 'R' else 0) * (2 ** l)
    print(f'column {suma}')
    return suma

def get_seat_id(input_values):
    max_id = 0
    for val in input_values:
        row = get_row(val[0:7])
        column = get_column(val[7:])
        seat_id = row * 8 + column
        max_id = max(max_id, seat_id)
    return max_id

def get_my_seat_id(input_values):
    l = [] 
    for val in input_values:
        row = get_row(val[0:7])
        column = get_column(val[7:])
        seat_id = row * 8 + column
        l.append(seat_id)

    l.sort()
    print(l)
    for i in range(len(l)):
        if  l[i+1] != l[i]+1: return l[i]+1

r = get_my_seat_id(input_values)
print(r)

r = get_my_seat_id(puzzle_values)
print(r)
# r = get_seat_id(input_values)
# print(r)

# r = get_seat_id(puzzle_values)
# print(r)
