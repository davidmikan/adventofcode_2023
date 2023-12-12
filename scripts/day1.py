import os
import sys
import re
import math

# load input file from "../inputs/dayXX.txt" relative to the python file's location
def load_input():
    file_directory = os.path.dirname(os.path.realpath(__file__))
    relative_path = "../inputs/day1.txt"
    absolute_path = os.path.normpath(os.path.join(file_directory, relative_path))
    with open(absolute_path) as f:
        return f.read().splitlines()

# go through the string and return if the character is a digit or the substring starts with a spelled out number
def find_num_or_word(s, step=1):
    numstrings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    start = 0 if step > 0 else len(s)-1
    stop = len(s) if step > 0 else -1
    for i in range(start, stop, step):
        if s[i].isdigit():
            return int(s[i])
        else:
            for j in range(len(numstrings)):
                if s[i:].startswith(numstrings[j]):
                    return j+1
                
def find_num(s, step=1):
    start = 0 if step > 0 else len(s)-1
    stop = len(s) if step > 0 else -1
    for i in range(start, stop, step):
        if s[i].isdigit():
            return int(s[i])

def part1(inp):
    return sum(find_num(s)*10 + find_num(s, -1) for s in inp)

def part2(inp):
    return sum(find_num_or_word(s)*10 + find_num_or_word(s, -1) for s in inp)

if __name__ == '__main__':
    # test_inp = ""
    # print("Solution for part 1 test input:", part1(test_inp))
    # print("Solution for part 2 test input:", part2(test_inp))

    inp = load_input()
    print("Solution to part 1:", part1(inp))
    print("Solution to part 2:", part2(inp))