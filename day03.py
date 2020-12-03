from typing import List, Tuple


def part1(trees: List[str]):
    total_trees = 0

    height = len(trees)
    width = len(trees[0])

    for i in range(1, height):
        j = (i * 3) % width
        if trees[i][j] == '#':
            total_trees += 1

    print(total_trees)


def getSlope(trees: List[str], right: int, down: int) -> int:
    total_trees = 0

    height = len(trees)
    width = len(trees[0])

    for i in range(down, height, down):
        j = ((i // down) * right) % width
        if trees[i][j] == '#':
            total_trees += 1

    return total_trees


def part2(trees: List[str]):
    paths: List[Tuple[int, int]] = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total = 1

    for path in paths:
        total *= getSlope(trees, *path)

    print(total)


def main():
    f = open('inputs/day03.txt')
    trees = [x.strip() for x in f.readlines()]

    part1(trees)
    part2(trees)


if __name__ == "__main__":
    main()
