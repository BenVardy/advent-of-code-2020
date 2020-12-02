from typing import List, Tuple

import re

regex = re.compile(r'^(\d+)-(\d+) ([a-z]): (.+)$')


def parseline(line: str) -> Tuple[int, int, str, str]:
    captures = regex.match(line)
    if captures is not None:
        return (
            int(captures.group(1)),
            int(captures.group(2)),
            captures.group(3),
            captures.group(4)
        )
    else:
        raise Exception('Invalid')


def part1(lines: List[Tuple[int, int, str, str]]):
    num_good = 0
    for line in lines:
        letter = line[2]
        val = line[3]
        count = val.count(letter)
        if count >= line[0] and count <= line[1]:
            num_good += 1

    print(num_good)


def part2(lines: List[Tuple[int, int, str, str]]):
    num_good = 0
    for line in lines:
        letter = line[2]
        val = line[3]

        at_a = val[line[0] - 1] == letter
        at_b = val[line[1] - 1] == letter

        if at_a and not at_b or not at_a and at_b:
            num_good += 1

    print(num_good)


def main():
    f = open('inputs/day02.txt')
    lines = [parseline(x.strip()) for x in f.readlines()]

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
