from typing import List

import itertools


def part1(lines: List[int]) -> int:
    for i, n in enumerate(lines[25:]):
        prev = lines[i:i+25]

        valid = False
        for x, y in itertools.combinations(prev, 2):
            if x + y == n:
                valid = True
                break

        if not valid:
            print(n)
            return n

    raise Exception('There should be an invalid number')


def part2(lines: List[int]):
    invalid = part1(lines)

    length = 2
    for i in range(len(lines)):
        while sum(lines[i:length]) < invalid:
            length += 1

        if sum(lines[i:length]) == invalid:
            print(min(lines[i:length]) + max(lines[i:length]))
            break


def main():
    f = open('inputs/day09.txt')

    lines = [int(x.strip()) for x in f.readlines()]

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
