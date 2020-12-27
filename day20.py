from __future__ import annotations
from typing import Deque, Dict, Generator, List, Optional, Tuple, Union

from copy import deepcopy
import math
import itertools
import re

from collections import deque


class Tile(object):
    def __init__(self, id: str, image: List[str]) -> None:
        self.image = deepcopy(image)
        self.id = id

    def rotate(self, n: int) -> Tile:
        if n % 4 == 0:
            return self
        elif n == 1:
            output: List[str] = []
            for j in range(len(self.image[0])):
                temp = ''
                for i in range(len(self.image)):
                    temp += self.image[i][j]
                output.append(temp[::-1])
            return Tile(self.id, output)

        t = self
        for i in range(n % 4):
            t = t.rotate(1)

        return t

    def flip_y(self) -> Tile:
        return Tile(self.id, self.image[::-1])

    def flip_x(self) -> Tile:
        return Tile(self.id, [x[::-1] for x in self.image])

    def get_side(self, side: int) -> str:
        if side == 0:
            return self.image[0]
        elif side == 1:
            return ''.join(x[-1] for x in self.image)
        elif side == 2:
            return self.image[-1][::-1]
        else:
            return ''.join(x[0] for x in self.image[::-1])

    def compare(self, other: Tile, side: int) -> bool:
        if side == 2 or side == 0:
            other_side = 2 - side
        else:
            other_side = 4 - side

        my_side = self.get_side(side)
        their_side = other.get_side(other_side)

        return my_side == their_side

    def image_nob(self) -> List[str]:
        return [row[1:-1] for row in self.image[1:-1]]

    def joined_image(self) -> str:
        return '\n'.join(self.image)

    def orientations(self) -> List[Tile]:
        return [
            self,
            self.rotate(1),
            self.rotate(1).flip_x(),
            self.rotate(1).flip_y(),
            self.rotate(2),
            self.rotate(2).flip_x(),
            self.rotate(2).flip_y(),
            self.rotate(3),
            self.rotate(3).flip_x(),
            self.rotate(3).flip_y(),
            self.flip_x(),
            self.flip_x().rotate(1),
            self.flip_x().rotate(2),
            self.flip_x().rotate(3),
            self.flip_y(),
            self.flip_y().rotate(1),
            self.flip_y().rotate(2),
            self.flip_y().rotate(3)
        ]

    def __str__(self) -> str:
        return f'Tile {self.id}:\n' + '\n'.join(self.image) + '\n\n'


def part1(tiles: List[Tile]):
    matching: Dict[str, List[Tuple[Tile, int]]] = {}
    for t, o in itertools.combinations(tiles, 2):
        if t.id not in matching:
            matching[t.id] = []
        elif len(matching[t.id]) == 4:
            continue

        if o.id not in matching:
            matching[o.id] = []
        elif len(matching[o.id]) == 4:
            continue

        done = False
        for _next in o.orientations():
            for i in range(0, 4):
                if t.compare(_next, i):
                    matching[t.id].append((_next, i))
                    if i == 2 or i == 0:
                        other_side = 2 - i
                    else:
                        other_side = 4 - i
                    matching[o.id].append((t, other_side))
                    done = True
                    break

            if done:
                break

        if done:
            continue

    corners = [k for k, v in matching.items() if len(v) == 2]
    print(math.prod(int(x) for x in corners))


def find_match(t: Tile, o: Tile, i: int) -> Optional[Tile]:
    for _next in o.orientations():
        if t.compare(_next, i):
            return _next

    return None


def part2(tiles: List[Tile]):
    matching: Dict[str, List[Optional[Tile]]] = dict.fromkeys((x.id for x in tiles))
    for k in matching.keys():
        matching[k] = [None] * 4
    tile_q: Deque[Tuple[str, Tile]] = deque([])

    first = tiles.pop(0)
    tile_q.append((first.id, first))

    found: Dict[str, Tile] = {first.id: first}
    not_found = deque((x.id, x) for x in tiles)

    while len(tile_q) != 0:
        _id, tile = tile_q.popleft()
        if all(x is not None for x in matching[_id]):
            continue

        for other_id, x in found.items():
            if other_id == _id:
                continue

            t_found = False
            for i, y in enumerate(matching[_id]):
                if y is None and tile.compare(x, i):
                    if i == 2 or i == 0:
                        other = 2 - i
                    else:
                        other = 4 - i

                    matching[_id][i] = x
                    matching[other_id][other] = tile
                    t_found = True
                    break
            if t_found:
                continue

        if all(x is not None for x in matching[_id]):
            continue

        for _ in range(len(not_found)):
            other_id, x = not_found.popleft()
            t_found = False
            for i, y in enumerate(matching[_id]):
                if y is None:
                    match = find_match(tile, x, i)
                    if match is not None:
                        if i == 2 or i == 0:
                            other = 2 - i
                        else:
                            other = 4 - i

                        matching[_id][i] = match
                        matching[other_id][other] = tile

                        tile_q.append((other_id, match))
                        found[other_id] = match
                        t_found = True
                        break

            if t_found:
                continue
            else:
                not_found.append((other_id, x))

    _map: List[List[Tuple[str, Tile]]] = []
    top_left: Optional[Tile] = None

    for _id, t in matching.items():
        if t[0] is None and t[3] is None and t[2] is not None and t[1] is not None:
            top_left = found[_id]

    _next: Optional[Tile] = top_left
    even = True
    while _next is not None:
        next_line = []
        while _next is not None:
            next_line.append((_next.id, _next))
            if even:
                _next = matching[_next.id][1]
            else:
                _next = matching[_next.id][3]

        _map.append(next_line)
        _next = matching[next_line[0][0]][2]
        even = not even

    h = 8
    out_map: List[str] = []

    for j, row in enumerate(_map):
        for i in range(h):
            line = ''
            for index, temp in enumerate(row):
                if j % 2 == 0:
                    if index % 2 == 1:
                        line += temp[1].flip_y().image_nob()[i]
                    else:
                        line += temp[1].image_nob()[i]
                else:
                    if index % 2 == 1:
                        line += temp[1].flip_x().flip_y().image_nob()[i]
                    else:
                        line += temp[1].flip_x().image_nob()[i]

            out_map.append(line)

    f_tile = Tile('0', out_map)

    middle_line_re = re.compile(r'^#(?:[#.]{4}##){3}#')
    bottom_line_re = re.compile(r'^[#.]#(?:[#.]{2}#){5}')

    for o in f_tile.orientations():
        no_monsters = 0
        image = o.image
        for i, line in enumerate(image[:-2]):
            for p, v in enumerate(line[18:]):
                if v != '#':
                    continue

                if not middle_line_re.match(image[i + 1][p:]):
                    continue

                if not bottom_line_re.match(image[i + 2][p:]):
                    continue

                no_monsters += 1

        if no_monsters != 0:
            total_hash = o.joined_image().count('#')
            print(total_hash - no_monsters * 15)
            break

def main():
    f = open('inputs/day20.txt')

    tiles: List[Tile] = []
    for t in f.read().split('\n\n'):
        lines = t.strip().split('\n')
        _id = lines[0].split(' ')[1][:-1]
        image = [x for x in lines[1:]]
        tiles.append(Tile(_id, image))

    part1(tiles)
    part2(tiles)


if __name__ == "__main__":
    main()
