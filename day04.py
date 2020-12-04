from typing import List, Dict

import re

passport_part = re.compile(r'([a-z]{3}):([^ \n]+)')


def readpassport(init: str) -> Dict[str, str]:
    output: Dict[str, str] = {}

    for x in passport_part.findall(init):
        output[x[0]] = x[1]

    return output


def part1(passports: List[Dict[str, str]]):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    no_valid = 0

    for passport in passports:
        keys = dict.keys(passport)
        valid = True
        for x in required:
            if x not in keys:
                valid = False

        if valid:
            no_valid += 1

    print(no_valid)


def part2(passports: List[Dict[str, str]]):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    regex = {
        'byr': re.compile(r'^(19[2-9]\d|200[012])$'),
        'iyr': re.compile(r'^20(1\d|20)$'),
        'eyr': re.compile(r'^20(2\d|30)$'),
        'hgt': re.compile(r'^(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)$'),
        'hcl': re.compile(r'^#[0-9a-f]{6}$'),
        'ecl': re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$'),
        'pid': re.compile(r'^\d{9}$')
    }

    no_valid = 0
    for passport in passports:
        keys = dict.keys(passport)
        valid = True
        for x in required:
            if x not in keys:
                valid = False
                break
            elif regex[x].match(passport[x]) is None:
                valid = False
                break

        if valid:
            no_valid += 1

    print(no_valid)


def main():
    f = open('inputs/day04.txt')
    all_text = ''.join(f.readlines())

    passports = [readpassport(x) for x in all_text.split('\n\n')]
    part1(passports)
    part2(passports)


if __name__ == "__main__":
    main()
