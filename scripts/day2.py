import os
import sys
import re
import math

# load input file from "../inputs/day2.txt"
def load_input():
    file_directory = os.path.dirname(os.path.realpath(__file__))
    relative_path = "../inputs/day2.txt"
    absolute_path = os.path.normpath(os.path.join(file_directory, relative_path))
    with open(absolute_path) as f:
        return f.read().splitlines()

def oob(x, y, inp):
    return x < 0 or x >= len(inp[0]) or y < 0 or y >= len(inp)

def validator_adjacent(x, y, inp):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (x==0 and y==0) or oob(x+dx, y+dy, inp) or inp[y+dy][x+dx] == '.':
                continue
            if not inp[y+dy][x+dx].isdigit():
                return True
    return False

def expand_num(x, y, inp):
    # expand the number to the right and left as long as there are digits next to it
    # return the expanded number and the new x position
    num = ''
    # go to the left while the next character is a digit
    while not oob(x-1, y, inp) and inp[y][x-1].isdigit():
        x -= 1
    while not oob(x, y, inp) and inp[y][x].isdigit():
        num += inp[y][x]
        x += 1
    return int(num), x-1

def num_adjacent(x, y, inp):
    total = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if (x==0 and y==0) or oob(x+dx, y+dy, inp) or inp[y+dy][x+dx] == '.':
                continue
            if inp[y+dy][x+dx].isdigit():
                total += 1
    return total

def part1(inp):
    total_sum = 0
    x, y = 0, 0
    while y < len(inp):
        while x < len(inp[y]):
            num = ''
            any_valid = False
            while not oob(x, y, inp) and inp[y][x].isdigit():
                num += inp[y][x]
                any_valid = any_valid or validator_adjacent(x, y, inp)
                x += 1
            total_sum += int(num) if any_valid else 0
            x += 1
        y += 1  
        x = 0       
    return total_sum

def part2(inp):
    # find all '*' and the amount of numbers they touch
    # if they touch exactly two numbers, add their product to the total sum
    total_sum = 0
    x, y = 0, 0
    while y < len(inp):
        while x < len(inp[y]):
            num = ''
            nums_touching = []
            while not oob(x, y, inp) and inp[y][x].isdigit():
                num += inp[y][x]
                num_touching += 1 if validator_adjacent(x, y, inp) else 0
                x += 1
            total_sum += int(num) if num_touching == 2 else 0
            x += 1
        y += 1  
        x = 0

if __name__ == '__main__':
    test_inp = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()

    print(expand_num(0, 0, test_inp))
    print(expand_num(8, 2, test_inp))

    print("Solution for part 1 test input:", part1(test_inp))
    print("Solution for part 2 test input:", part2(test_inp))

    inp = load_input()
    print("Solution to part 1:", part1(inp))
    print("Solution to part 2:", part2(inp))