from typing import List


def part1(groups: List[str]):
    total = 0
    for group in groups:
        no_newline = group.replace('\n', '')
        total += len(set(no_newline))

    print(total)


def part2(groups: List[str]):
    total = 0

    for group in groups:
        people = group.split('\n')
        common = list(people[0])

        for person in people[1:]:
            common = [x for x in common if person.count(x) > 0]
            if len(common) == 0:
                break

        total += len(common)

    print(total)


def main():
    f = open('inputs/day06.txt')

    groups = f.read().strip().split('\n\n')

    part1(groups)
    part2(groups)

    f.close()


if __name__ == "__main__":
    main()
