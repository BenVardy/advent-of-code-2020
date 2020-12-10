from typing import Dict, List


def part1(lines: List[int]):
    current = 0

    one = 0
    three = 1

    while len(lines) > 0:
        allowed = [x for x in lines if current + 3 >= x and current < x]
        use = min(allowed)
        if use - current == 1:
            one += 1
        elif use - current == 3:
            three += 1

        current = use
        lines = [x for x in lines if x != current]

    print(one, three, one * three)


total_arrangements: Dict[int, int] = {}


def count_arrangements(lines: List[int], c: int) -> int:
    if c in total_arrangements.keys():
        return total_arrangements[c]

    valid_next = [x for x in lines if c + 3 >= x and c < x]

    total = 0
    for x in valid_next:
        x_total = count_arrangements(lines, x)
        total_arrangements[x] = x_total
        total += x_total

    return total


def part2(lines: List[int]):
    target = max(lines)
    total_arrangements[target] = 1

    arrangements = count_arrangements(lines, 0)
    print(arrangements)


def main():
    f = open('inputs/day10.txt')
    lines = [int(x.strip()) for x in f.readlines()]

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
