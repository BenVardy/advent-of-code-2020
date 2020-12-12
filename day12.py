from typing import List, Tuple


Commands = List[Tuple[str, int]]


class Ship(object):
    right = {
        'N': 'E',
        'E': 'S',
        'S': 'W',
        'W': 'N'
    }

    left = {
        'N': 'W',
        'W': 'S',
        'S': 'E',
        'E': 'N'
    }

    def __init__(self) -> None:
        self.dir = 'E'
        self.pos: Tuple[int, int] = (0, 0)

    def move(self, dir: str, n: int) -> None:
        if dir in 'FLR':
            if dir == 'F':
                self.move(self.dir, n)
            elif dir in 'LR':
                for _ in range(0, n // 90):
                    self.__turn(dir)

            return

        to_add: Tuple[int, int] = (0, 0)

        if dir == 'N':
            to_add = (0, n)
        elif dir == 'S':
            to_add = (0, -n)
        elif dir == 'E':
            to_add = (n, 0)
        elif dir == 'W':
            to_add = (-n, 0)

        self.pos = (self.pos[0] + to_add[0], self.pos[1] + to_add[1])

    def getmanhatten(self) -> int:
        return abs(self.pos[0]) + abs(self.pos[1])

    def __turn(self, dir: str):
        if dir == 'R':
            self.dir = self.right[self.dir]
        elif dir == 'L':
            self.dir = self.left[self.dir]


class Waypoint(Ship):
    def __init__(self) -> None:
        self.ship = Ship()
        super().__init__()
        self.pos = (10, 1)

    def move(self, dir: str, n: int) -> None:
        if dir in 'NSEW':
            return super(Waypoint, self).move(dir, n)

        if dir == 'F':
            self.ship.pos = (
                self.ship.pos[0] + self.pos[0] * n,
                self.ship.pos[1] + self.pos[1] * n
            )
        elif dir in 'RL':
            for _ in range(n // 90):
                self.__turn(dir)

    def getmanhatten(self) -> int:
        return self.ship.getmanhatten()

    def __turn(self, dir: str) -> None:
        if dir == 'R':
            self.pos = (self.pos[1], -self.pos[0])
        elif dir == 'L':
            self.pos = (-self.pos[1], self.pos[0])


def part1(lines: Commands):
    ship = Ship()

    for x in lines:
        ship.move(*x)

    print(ship.getmanhatten())


def part2(lines: Commands):
    waypoint = Waypoint()

    for x in lines:
        waypoint.move(*x)

    print(waypoint.getmanhatten())


def main():
    f = open('inputs/day12.txt')

    lines: Commands = [(x[0], int(x[1:-1])) for x in f.readlines()]

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main()
