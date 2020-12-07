from typing import List

import re


def findbag(lines: List[str], bag: str) -> List[str]:
    regex = re.compile(r'(\w+ \w+) bags contain .*\d+ (' + bag + r')')

    found: List[str] = []
    for x in regex.findall(''.join(lines)):
        found.append(x[0])

    return found


def part1(lines: List[str]):
    accept: List[str] = []

    to_find = ['shiny gold']
    while len(to_find) != 0:
        new_found: List[str] = []
        for x in to_find:
            found = findbag(lines, x)
            new_found += [y for y in found if y not in accept]
            accept += found

        to_find = new_found

    print(len(set(accept)))


def calc_bag(lines: List[str], bag: str) -> int:
    regex = re.compile(r'(\d+) (\w+ \w+) bags?')
    bag_re = re.compile(bag + r' bags contain')

    bag_line = ''
    for line in lines:
        if bag_re.match(line) is not None:
            bag_line = line
            break

    all_bags = regex.findall(bag_line)
    if len(all_bags) == 0:
        return 0
    else:
        return sum(calc_bag(lines, x[1]) * int(x[0]) + int(x[0]) for x in all_bags)


def part2(lines: List[str]):
    print(calc_bag(lines, 'shiny gold'))


def main():
    f = open('inputs/day07.txt')

    lines = f.readlines()

    part1(lines)
    part2(lines)



if __name__ == "__main__":
    main()
