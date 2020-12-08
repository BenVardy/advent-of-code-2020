from typing import List, Union


def part1(lines: List[str]):
    acc = 0
    i = 0

    executed: List[int] = []

    while i < len(lines):
        if i in executed:
            print(acc)
            break

        command = lines[i].split(' ')
        operand = command[0]
        opcode = int(command[1])

        executed.append(i)

        if operand == 'acc':
            acc += opcode
            i += 1
        elif operand == 'jmp':
            i += opcode
        elif operand == 'nop':
            i += 1


def execute(lines: List[str]) -> Union[None, int]:
    acc = 0
    i = 0

    executed: List[int] = []

    while i < len(lines):
        if i in executed:
            return None

        command = lines[i].split(' ')
        operand = command[0]
        opcode = int(command[1])

        executed.append(i)

        if operand == 'acc':
            acc += opcode
            i += 1
        elif operand == 'jmp':
            i += opcode
        elif operand == 'nop':
            i += 1

    return acc


def part2(lines: List[str]):
    for i in range(len(lines)):
        new_lines = lines[:]

        line = new_lines[i]
        if 'acc' in line:
            continue
        elif 'jmp' in line:
            new_lines[i] = line.replace('jmp', 'nop')
        elif 'nop' in line:
            new_lines[i] = line.replace('nop', 'jmp')

        out = execute(new_lines)
        if out is not None:
            print(out)
            break


def main():
    f = open('inputs/day08.txt')

    lines = [x.strip() for x in f.readlines()]

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
