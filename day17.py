from typing import List, Tuple

import copy
import itertools

PocketDimension = List[List[bool]]
Coord = Tuple[int, int, int]


def countneighbours(cubes: List[PocketDimension], c: Coord) -> int:
    l = (len(cubes[0][0]), len(cubes[0]), len(cubes))
    total = 0
    for x, y, z in itertools.product(range(-1, 2), range(-1, 2), range(-1, 2)):
        if (x, y, z) == (0, 0, 0):
            continue

        n_x = c[0] + x
        n_y = c[1] + y
        n_z = abs(c[2] + z)

        n = (n_x, n_y, n_z)
        if any(n_i < 0 for n_i in n):
            continue

        if any(n_i >= l_i for n_i, l_i in zip(n, l)):
            continue

        if cubes[n_z][n_y][n_x]:
            total += 1

    return total


def increase_cubes(cubes: List[PocketDimension]) -> List[PocketDimension]:
    l_init = (len(cubes[0][0]), len(cubes[0]), len(cubes))
    n_cubes = copy.deepcopy(cubes)
    for y, z in itertools.product(range(l_init[1]), range(l_init[2])):
        n_cubes[z][y] = [False] + cubes[z][y] + [False]

    for z in range(l_init[2]):
        n_cubes[z] = [[False] * (l_init[0] + 2)] + n_cubes[z] + [[False] * (l_init[0] + 2)]

    n_cubes.append([[False] * (l_init[0] + 2) for y in range(l_init[1] + 2)])

    return n_cubes


def part1(cubes: List[PocketDimension]):
    prev: List[PocketDimension] = []
    for i in range(6):
        cubes= increase_cubes(cubes)
        l = (len(cubes[0][0]), len(cubes[0]), len(cubes))
        prev = copy.deepcopy(cubes)
        for c in itertools.product(range(l[0]), range(l[1]), range(l[2])):
            neighbours = countneighbours(prev, c)
            cube = prev[c[2]][c[1]][c[0]]
            if cube and neighbours in (2, 3) or not cube and neighbours == 3:
                cubes[c[2]][c[1]][c[0]] = True
            else:
                cubes[c[2]][c[1]][c[0]] = False

    total = 0
    l = (len(cubes[0][0]), len(cubes[0]), len(cubes))
    for x, y in itertools.product(range(l[0]), range(l[1])):
        if cubes[0][y][x]:
            total += 1

    for x, y, z in itertools.product(range(l[0]), range(l[1]), range(1, l[2])):
        if cubes[z][y][x]:
            total += 2

    print(total)


HPocketDim = List[List[List[bool]]]
HCoord = Tuple[int, int, int, int]


def countneighbours_p2(hcubes: List[HPocketDim], c: HCoord) -> int:
    l = (len(hcubes[0][0][0]), len(hcubes[0][0]), len(hcubes[0]), len(hcubes))
    total = 0
    for x, y, z, w in itertools.product(range(-1, 2), range(-1, 2), range(-1, 2), range(-1, 2)):
        if (x, y, z, w) == (0, 0, 0, 0):
            continue

        n_x = c[0] + x
        n_y = c[1] + y
        n_z = c[2] + z
        n_w = abs(c[3] + w)

        n = (n_x, n_y, n_z, n_w)
        if any(n_i < 0 for n_i in n):
            continue

        if any(n_i >= l_i for n_i, l_i in zip(n, l)):
            continue

        if hcubes[n_w][n_z][n_y][n_x]:
            total += 1

    return total


def increase_hcubes(hcubes: List[HPocketDim]) -> List[HPocketDim]:
    l_init = (len(hcubes[0][0][0]), len(hcubes[0][0]), len(hcubes[0]), len(hcubes))
    n_cubes = copy.deepcopy(hcubes)
    for y, z, w in itertools.product(range(l_init[1]), range(l_init[2]), range(l_init[3])):
        n_cubes[w][z][y] = [False] + hcubes[w][z][y] + [False]

    for z, w in itertools.product(range(l_init[2]), range(l_init[3])):
        n_cubes[w][z] = [[False] * (l_init[0] + 2)] + n_cubes[w][z] + [[False] * (l_init[0] + 2)]

    for w in range(l_init[3]):
        n_cubes[w] = \
            [[[False] * (l_init[0] + 2) for y in range(l_init[1] + 2)]] + \
            n_cubes[w] + \
            [[[False] * (l_init[0] + 2) for y in range(l_init[1] + 2)]]

    n_cubes.append([[[False] * (l_init[0] + 2) for y in range(l_init[1] + 2)] for z in range(l_init[2] + 2)])

    return n_cubes


def part2(hcubes: List[HPocketDim]):
    prev: List[HPocketDim] = []
    for i in range(6):
        hcubes = increase_hcubes(hcubes)
        l = (len(hcubes[0][0][0]), len(hcubes[0][0]), len(hcubes[0]), len(hcubes))
        prev = copy.deepcopy(hcubes)
        for c in itertools.product(range(l[0]), range(l[1]), range(l[2]), range(l[3])):
            neighbours = countneighbours_p2(prev, c)
            cube = prev[c[3]][c[2]][c[1]][c[0]]
            if cube and neighbours in (2, 3) or not cube and neighbours == 3:
                hcubes[c[3]][c[2]][c[1]][c[0]] = True
            else:
                hcubes[c[3]][c[2]][c[1]][c[0]] = False

    total = 0
    l = (len(hcubes[0][0][0]), len(hcubes[0][0]), len(hcubes[0]), len(hcubes))
    for x, y, z in itertools.product(range(l[0]), range(l[1]), range(l[2])):
        if hcubes[0][z][y][x]:
            total += 1

    for x, y, z, w in itertools.product(range(l[0]), range(l[1]), range(l[2]), range(1, l[3])):
        if hcubes[w][z][y][x]:
            total += 2

    print(total)


def main():
    f = open('inputs/day17.txt')

    cubes: List[PocketDimension] = [[[x == '#' for x in line.strip()] for line in f.readlines()]]

    part1(cubes)
    part2([cubes])


if __name__ == "__main__":
    main()
