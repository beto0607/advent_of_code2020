import re
input_values = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc',
]

puzzle_values = [line.strip() for line in open("input.txt", "r")]


def get_count(input_values):
    count = 0

    for line in input_values:
        arr = line.split(' ')
        [min_v, max_v] = arr[0].split('-')
        [letter] = arr[1][0]
        word = arr[2]
        c = word.count(letter)
        if int(min_v) <= c <= int(max_v):
            count += 1

    return count


def get_count2(input_values):
    count = 0
    for line in input_values:
        arr = line.split(' ')
        [min_v, max_v] = arr[0].split('-')
        min_v = int(min_v)-1
        max_v = int(max_v)-1
        [letter] = arr[1][0]
        word = arr[2]
        if bool(word[min_v] == letter) ^ bool(word[max_v] == letter):
            count += 1
    return count


res = get_count2(input_values)
print(res)
res = get_count2(puzzle_values)
print(res)
