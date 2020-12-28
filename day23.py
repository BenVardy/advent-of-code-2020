from typing import List


def part1(cups: List[int]):
    cups = cups[:]

    current_index = 0
    no_cups = len(cups)
    for _ in range(100):
        current_cup = cups[current_index]
        remove_indices = [(current_index + i) % no_cups for i in range(1, 4)]
        next_three = [cups[i] for i in remove_indices]

        # for x in next_three:
        #     cups.remove(x)

        if remove_indices[0] < remove_indices[2]:
            cups = cups[:remove_indices[0]] + cups[remove_indices[2] + 1:]
        else:
            cups = cups[remove_indices[2] + 1:remove_indices[0]]

        next_index = -1
        for j in range(1, no_cups + 1):
            next_cup = (current_cup - j - 1) % no_cups + 1
            if next_cup not in next_three:
                next_index = cups.index(next_cup)
                break

        cups[next_index+1:next_index+1] = next_three
        if next_index < current_index:
            current_index += min(no_cups - current_index - 1, 3)

        current_index = (current_index + 1) % no_cups

    one_index = cups.index(1)
    output = ''
    for i in range(1, no_cups):
        output += str(cups[(one_index + i) % no_cups])

    print(output)


# This was not my code - taken from https://github.com/frerich/aoc2020/blob/main/day23.py
def part2(cups: List[int]):
    cups = cups[:]
    succ: List[int] = [0] * (len(cups) + 1)

    for i in range(len(cups) - 1):
        succ[cups[i]] = cups[i + 1]

    succ[cups[-1]] = cups[0]

    _max = max(succ)
    succ.extend(range(_max + 2, 1_000_000 + 2))
    succ[cups[-1]] = _max + 1
    succ[1_000_000] = cups[0]

    current_cup = cups[0]
    for _ in range(10000000):
        p0 = succ[current_cup]
        p1 = succ[p0]
        p2 = succ[p1]

        _next = succ[p2]

        dest = current_cup - 1
        while True:
            if dest < 1:
                dest = max(succ)
            if dest not in (p0, p1, p2):
                break
            dest -= 1

        succ[current_cup] = _next
        succ[p2] = succ[dest]
        succ[dest] = p0
        current_cup = _next

    first = succ[1]
    second = succ[first]
    print(first * second)


def main():
    f = open('inputs/day23.txt')
    cups = [int(x) for x in list(f.readline().strip())]

    # part1(cups)
    part2(cups)


if __name__ == "__main__":
    main()
