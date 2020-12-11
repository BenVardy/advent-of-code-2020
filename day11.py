from typing import List, Tuple

from copy import deepcopy


def valid_coord(l_1: int, l_2: int, x: int, y: int) -> bool:
    return x >= 0 and y >= 0 and x < l_1 and y < l_2


def p1_count(seats: List[List[str]], pos: Tuple[int, int]) -> int:
    total = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            x = pos[0] + i
            y = pos[1] + j
            if not (i == 0 and i == j) and valid_coord(len(seats), len(seats[0]), x, y):
                if seats[x][y] == '#':
                    total += 1

    return total


def part1(seats: List[List[str]]):
    prev: List[List[str]] = []
    while prev != seats:
        prev = deepcopy(seats)
        for i, x in enumerate(prev):
            for j, y in enumerate(x):
                if y != '.':
                    n = p1_count(prev, (i, j))
                    if y == 'L' and n == 0:
                        seats[i][j] = '#'
                    elif y == '#' and n >= 4:
                        seats[i][j] = 'L'

    total = 0
    for x in seats:
        for y in x:
            if y == '#':
                total += 1

    print(total)


def p2_count(seats: List[List[str]], x: int, y: int) -> int:
    total = 0
    l_1 = len(seats)
    l_2 = len(seats[0])

    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and i == j):
                n_x = x + i
                n_y = y + j

                while valid_coord(l_1, l_2, n_x, n_y) and seats[n_x][n_y] == '.':
                    n_x += i
                    n_y += j

                if valid_coord(l_1, l_2, n_x, n_y) and seats[n_x][n_y] == '#':
                    total += 1

    return total


def part2(seats: List[List[str]]):
    prev: List[List[str]] = []
    while prev != seats:
        prev = deepcopy(seats)
        for i, x in enumerate(prev):
            for j, y in enumerate(x):
                if y != '.':
                    n = p2_count(prev, i, j)
                    if y == 'L' and n == 0:
                        seats[i][j] = '#'
                    elif y == '#' and n >= 5:
                        seats[i][j] = 'L'

    total = 0
    for x in seats:
        for y in x:
            if y == '#':
                total += 1

    print(total)


def main():
    f = open('inputs/day11.txt')

    seats = [list(x.strip()) for x in f.readlines()]

    part1(deepcopy(seats))
    part2(deepcopy(seats))


if __name__ == "__main__":
    main()
