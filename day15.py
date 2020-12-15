from typing import Dict, List, Tuple


def mem_game(s_n: List[int], to: int) -> int:
    said: Dict[int, Tuple[int, int]] = {}

    for i, n in enumerate(s_n):
        said[n] = (-1, i)

    prev = s_n[-1]
    for i in range(len(s_n), to):
        info = said[prev]
        if info[0] == -1:
            _next = 0
        else:
            _next = info[1] - info[0]

        if _next in said:
            said[_next] = (said[_next][1], i)
        else:
            said[_next] = (-1, i)

        prev = _next

    return prev


def part1(s_n: List[int]):
    out = mem_game(s_n, 2020)

    print(out)


def part2(s_n: List[int]):
    out = mem_game(s_n, 30000000)

    print(out)


def main():
    f = open('inputs/day15.txt')

    s_n = [int(x) for x in f.readline().strip().split(',')]

    part1(s_n)
    part2(s_n)


if __name__ == "__main__":
    main()
