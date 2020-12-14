from typing import List, Dict

import re

mem_re = re.compile(r'mem\[(\d+)\] = (\d+)')


def part1(lines: List[str]):
    memory: Dict[int, int] = {}

    mask = ''

    for l in lines:
        m = mem_re.match(l)
        if m is None:
            mask = l.split(' ')[2]
            continue

        addr = int(m.group(1))
        val = bin(int(m.group(2)))[2:]

        new_val = ''
        for x, v in zip(mask, val.zfill(len(mask))):
            if x == 'X':
                new_val += v
            else:
                new_val += x

        memory[addr] = int(new_val, 2)

    print(sum(memory.values()))


def part2(lines: List[str]):
    memory: Dict[int, int] = {}

    mask = ''

    for l in lines:
        m = mem_re.match(l)
        if m is None:
            mask = l.split(' ')[2]
            continue

        addr = bin(int(m.group(1)))[2:].zfill(len(mask))
        val = int(m.group(2))

        new_addr = ''
        for x, a in zip(mask, addr):
            if x == '0':
                new_addr += a
            else:
                new_addr += x

        n_x = new_addr.count('X')
        for i in range(1 << n_x):
            a_li = list(new_addr)
            b_i = bin(i)[2:].zfill(n_x)
            for j in range(n_x):
                a_li[a_li.index('X')] = b_i[j]

            memory[int(''.join(a_li), 2)] = val

    print(sum(memory.values()))


def main():
    f = open('inputs/day14.txt')

    lines = [x.strip() for x in f.readlines()]

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
