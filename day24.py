from typing import Dict, List, Set, Tuple

import re


directions_re = re.compile(r'e|se|sw|w|nw|ne')


def part1(lines: List[str]):
    coordinates: List[Tuple[int, int]] = []
    for line in lines:
        directions = directions_re.findall(line)
        x, y = 0, 0
        for direction in directions:
            if direction == 'e':
                x -= 2
            elif direction == 'w':
                x += 2
            elif direction == 'ne':
                x -= 1
                y -= 1
            elif direction == 'sw':
                x += 1
                y += 1
            elif direction == 'se':
                x -= 1
                y += 1
            elif direction == 'nw':
                x += 1
                y -= 1

        coordinates.append((x, y))

    total = 0
    for tile in set(coordinates):
        if coordinates.count(tile) % 2 == 1:
            total += 1

    print(total)


def count_neighbours(tile: Tuple[int, int], black_tiles: Set[Tuple[int, int]]) -> int:
    x, y = tile
    total = 0
    for d_x, d_y in [
        (-2, 0),
        (-1, -1),
        (1, -1),
        (2, 0),
        (1, 1),
        (-1, 1)
    ]:
        if (x + d_x, y + d_y) in black_tiles:
            total += 1

    return total


def part2(lines: List[str]):
    coordinates: List[Tuple[int, int]] = []
    for line in lines:
        directions = directions_re.findall(line)
        x, y = 0, 0
        for direction in directions:
            if direction == 'e':
                x -= 2
            elif direction == 'w':
                x += 2
            elif direction == 'ne':
                x -= 1
                y -= 1
            elif direction == 'sw':
                x += 1
                y += 1
            elif direction == 'se':
                x -= 1
                y += 1
            elif direction == 'nw':
                x += 1
                y -= 1

        coordinates.append((x, y))

    black_tiles: Set[Tuple[int, int]] = set()
    for tile in set(coordinates):
        if coordinates.count(tile) % 2 == 1:
            black_tiles.add(tile)

    print(len(black_tiles))

    for i in range(100):
        next_black_tiles: Set[Tuple[int, int]] = set()

        min_black_x = min(x for x, y in black_tiles)
        max_black_x = max(x for x, y in black_tiles)

        min_black_y = min(y for x, y in black_tiles)
        max_black_y = max(y for x, y in black_tiles)

        for y in range(min_black_y - 1, max_black_y + 2):
            temp_min_black_x = min_black_x
            if min_black_x % 2 != y % 2:
                temp_min_black_x -= 1

            for x in range(temp_min_black_x - 2, max_black_x + 4, 2):
                neighbours = count_neighbours((x, y), black_tiles)
                if (x, y) in black_tiles:
                    if neighbours > 0 and neighbours <= 2:
                        next_black_tiles.add((x, y))
                else:
                    if neighbours == 2:
                        next_black_tiles.add((x, y))

        black_tiles = next_black_tiles

    print(len(black_tiles))


def main():
    f = open('inputs/day24.txt')
    lines = f.read().strip().split('\n')

    # part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
