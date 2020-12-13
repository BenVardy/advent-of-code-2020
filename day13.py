from typing import List, Tuple

from functools import reduce


def part1(val: int, lines: List[str]):
    times = [int(x) for x in lines if x != 'x']

    mods: List[Tuple[int, int]] = [(x - (val % x), x) for x in times]
    _min = min(mods)

    print(_min[0] * _min[1])


# From https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p

    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1

    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += b0

    return x1


def part2(lines: List[str]):
    n = [int(x) for x in lines if x != 'x']
    a = [int(x) - i for i, x in enumerate(lines) if x != 'x']

    print(chinese_remainder(n, a))


def main():
    f = open('inputs/day13.txt')

    val = int(f.readline().strip())
    lines = f.readline().strip().split(',')

    part1(val, lines)
    part2(lines)


if __name__ == "__main__":
    main()
