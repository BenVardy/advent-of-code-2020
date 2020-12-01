import itertools


def part1(values):
    for x, y in itertools.combinations(values, 2):
        if x + y == 2020:
            print(x * y)
            break


def part2(values):
    for x, y, z, in itertools.combinations(values, 3):
        if x + y + z == 2020:
            print(x * y * z)
            break


def main():
    f = open('inputs/day01.txt')
    values = [int(x.strip()) for x in f.readlines()]
    part1(values)
    part2(values)

    f.close()


if __name__ == "__main__":
    main()
