from typing import List


def part1(passes: List[str], p=True) -> List[bool]:
    plane = [False] * (128 * 8)

    for _pass in passes:
        min_row = 0
        max_row = 127
        for x in _pass[:7]:
            if x == 'F':
                max_row = (max_row + min_row) // 2
            elif x == 'B':
                min_row = (max_row + min_row) // 2 + 1

        min_col = 0
        max_col = 7
        for x in _pass[-3:]:
            if x == 'L':
                max_col = (min_col + max_col) // 2
            elif x == 'R':
                min_col = (min_col + max_col) // 2 + 1

        plane[max_row * 8 + max_col] = True

    if p:
        print(max(i for i, x in enumerate(plane) if x))

    return plane


def part2(passes: List[str]):
    plane = part1(passes, False)
    print([
        i for i, x in enumerate(plane)
        if not x and
        (i - 1) >= 0 and
        (i + 1) < len(plane) and
        plane[i + 1] and
        plane[i - 1]
    ])


def main():
    f = open('inputs/day05.txt')

    passes = [x.strip() for x in f.readlines()]

    part1(passes)
    part2(passes)


if __name__ == "__main__":
    main()
