import functools
input_values = [
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#',
]

puzzle_values = [line.strip() for line in open("input.txt", "r")]

def count_trees(input_values, right=3, bottom=1):
    count = 0
    max_x = len(input_values[0])
    # print(max_x)
    # print(len(input_values))
    pos_x = 0
    pos_y = 0
    while pos_y+bottom < len(input_values):
        pos_x = (pos_x +right) % max_x
        pos_y += bottom
        # print(pos_x, pos_y)
        if(input_values[pos_y][pos_x] == '#'):
            count +=1
    return count

def multiply_counters(input_values):
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    res = [count_trees(input_values, right, bottom)  for [right, bottom] in slopes]
    print(res)
    return functools.reduce(lambda a, b: a*b, res)

# res = count_trees(input_values)
# print(res)
# res = count_trees(puzzle_values)
# print(res)
res = multiply_counters(input_values)
print(res)
res = multiply_counters(puzzle_values)
print(res)
