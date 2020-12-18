from typing import List

import re


def calculate(expr: str) -> int:
    start_b = 0
    no_b = 0
    old = expr
    for i, v in enumerate(old):
        if v == '(':
            if no_b == 0:
                start_b = i
            no_b += 1
        elif v == ')':
            no_b -= 1
            if no_b == 0:
                expr = expr.replace(old[start_b:i+1], str(calculate(old[start_b+1:i])), 1)

    vals = expr.split(' ')
    total: int = int(vals[0])
    op = ''
    for x in vals[1:]:
        if x in ('+', '*'):
            op = x
        else:
            total = eval(str(total) + op + x)

    return total


def part1(lines: List[str]):
    s = sum(calculate(line) for line in lines)
    print(s)


add_re = re.compile(r'\d+ \+ \d+')


def p2_calculate(expr: str) -> int:
    start_b = 0
    no_b = 0
    old = expr
    for i, v in enumerate(old):
        if v == '(':
            if no_b == 0:
                start_b = i
            no_b += 1
        elif v == ')':
            no_b -= 1
            if no_b == 0:
                expr = expr.replace(old[start_b:i+1], str(p2_calculate(old[start_b+1:i])), 1)

    x = add_re.search(expr)
    while x is not None:
        expr = expr.replace(x.group(0), str(eval(x.group(0))), 1)
        x = add_re.search(expr)

    return eval(expr)


def part2(lines: List[str]):
    s = sum(p2_calculate(line) for line in lines)
    print(s)


def main():
    f = open('inputs/day18.txt')

    lines = [x.strip() for x in f.readlines()]

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
