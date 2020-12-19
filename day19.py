from typing import Dict, List

from string import ascii_letters
from random import choice

import regex

letter_re = regex.compile(r'("[a-zA-Z]")|([a-zA-Z])')


expanded_rules: Dict[str, str] = {}
uuids: Dict[str, str] = {}


def expandrule(rules: Dict[str, str], rule: str) -> str:
    global uuids
    global expanded_rules
    if rule not in uuids:
        uuids[rule] = ''.join(choice(ascii_letters) for x in range(3))

    if rule in expanded_rules:
        return expanded_rules[rule]

    base = rules[rule]
    if letter_re.match(base):
        expanded_rules[rule] = base[1]
        return base[1]

    output = ''
    for n in base.split(' '):
        if n == '|':
            output += '|'
        elif n == rule:
            output += f'(?P>{uuids[rule]})'
        else:
            output += expandrule(rules, n)

    expanded_rules[rule] = f'(?<{uuids[rule]}>' + output + ')'
    return f'(?<{uuids[rule]}>' + output + ')'


def part1(rules: Dict[str, str], lines: List[str]):
    zero_re = regex.compile('^' + expandrule(rules, '0') + '$')

    total = 0
    for line in lines:
        if zero_re.match(line):
            total += 1

    print(total)


def part2(rules: Dict[str, str], lines: List[str]):
    rules['11'] = '42 31 | 42 11 31'
    rules['8'] = '42 | 42 8'
    global expanded_rules
    expanded_rules = {}
    zero_re = regex.compile('^' + expandrule(rules, '0') + '$')

    total = 0
    for line in lines:
        if zero_re.match(line):
            total += 1

    print(total)


def main():
    f = open('inputs/day19.txt')
    init = f.read().split('\n\n')
    rules: Dict[str, str] = {x.split(': ')[0]: x.split(': ')[1] for x in init[0].split('\n')}
    lines = init[1].split('\n')

    part1(rules, lines)
    part2(rules, lines)



if __name__ == "__main__":
    main()
