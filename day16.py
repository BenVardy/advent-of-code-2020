from typing import List, Tuple


Field = Tuple[str, Tuple[int, int], Tuple[int, int]]


def parsefields(lines: List[str]) -> List[Field]:
    out: List[Field] = []

    for line in lines:
        name, str_ranges = line.split(': ')
        ranges: List[Tuple[int, int]] = []
        for r in str_ranges.split(' or '):
            ranges.append(tuple(int(x) for x in r.split('-')))

        out.append((name, ranges[0], ranges[1]))

    return out


def validval(fields: List[Field], val: int) -> int:
    for f in fields:
        if val in range(f[1][0], f[1][1] + 1):
            return -1
        elif val in range(f[2][0], f[2][1] + 1):
            return -1

    return val


def part1(fields: List[Field], nearby: List[List[int]]):
    invalid = 0

    for ticket in nearby:
        for val in ticket:
            inv = validval(fields, val)
            if inv != -1:
                invalid += inv

    print(invalid)


def validcols(fields: List[Field], val: int) -> List[str]:
    valid: List[str] = []

    for f in fields:
        if val in range(f[1][0], f[1][1] + 1):
            valid.append(f[0])
        elif val in range(f[2][0], f[2][1] + 1):
            valid.append(f[0])

    return valid


def part2(fields: List[Field], mine: List[int], nearby: List[List[int]]):
    valid: List[List[int]] = [t for t in nearby if all(validval(fields, v) == -1 for v in t)]

    row_mat = [[validcols(fields, x) for x in row] for row in valid]

    w = len(row_mat[0])
    col_mat: List[List[List[str]]] = []
    for i in range(w):
        _new = []
        for j in range(len(row_mat)):
            _new.append(row_mat[j][i])
        col_mat.append(_new)

    found = []
    headings = []

    while len(found) != len(fields):
        for f, _, _ in fields:
            for i, col in enumerate(col_mat):
                if not all(f in x for x in col):
                    col_mat[i] = [[y for y in x if y != f] for x in col]

        for i, col in enumerate(col_mat):
            if all(len(x) == 1 for x in col):
                found.append(col[0][0])
                headings.append((col[0][0], i))

        col_mat = [[[y for y in x if y not in found] for x in col] for col in col_mat]

    headings.sort(key=lambda x: (x[1], x[0]))

    total = 1
    for h_v, v in zip(headings, mine):
        if 'departure' in h_v[0]:
            total *= v

    print(total)


def main():
    f = open('inputs/day16.txt')

    all_lines = f.read().strip()

    sections = all_lines.split('\n\n')
    fields = parsefields(sections[0].split('\n'))

    mine = [int(x) for x in sections[1].split('\n')[1].split(',')]

    nearby = [[int(y) for y in x.split(',')] for x in sections[2].split('\n')[1:]]

    # part1(fields, nearby)
    part2(fields, mine, nearby)



if __name__ == "__main__":
    main()
