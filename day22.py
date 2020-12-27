from __future__ import annotations
from typing import List, Tuple

from collections import deque


class Player(object):
    def __init__(self, cards: List[int]) -> None:
        self.cards = deque(cards[:])

    def draw(self) -> int:
        return self.cards.popleft()

    def add_cards(self, *cards: int) -> None:
        self.cards.extend(cards)

    def empty(self) -> bool:
        return len(self.cards) == 0

    def clone(self, n: int = -1) -> Player:
        if n == -1:
            return Player(list(self.cards))
        else:
            return Player(list(self.cards)[:n])

    def score(self) -> int:
        return sum(i * x for i, x in enumerate(list(self.cards)[::-1], 1))

    def left(self) -> int:
        return len(self.cards)

    def get_cards(self) -> List[int]:
        return list(self.cards)[:]

    def __str__(self) -> str:
        return self.cards.__str__()


def part1(p1: Player, p2: Player):
    p1 = p1.clone()
    p2 = p2.clone()

    while not (p1.empty() or p2.empty()):
        c1 = p1.draw()
        c2 = p2.draw()
        if c1 > c2:
            p1.add_cards(c1, c2)
        elif c2 > c1:
            p2.add_cards(c2, c1)
        else:
            raise Exception('I thought this might happen')

    if not p1.empty():
        print('p1 wins! Score:', p1.score())
    elif not p2.empty():
        print('p2 wins! Score:', p2.score())


def recursive_combat(p1: Player, p2: Player) -> str:
    rounds: List[Tuple[List[int], List[int]]] = []

    while not (p1.empty() or p2.empty()):
        cards = (p1.get_cards(), p2.get_cards())
        if cards in rounds:
            return 'p1'

        rounds.append(cards)
        c1 = p1.draw()
        c2 = p2.draw()
        if p1.left() >= c1 and p2.left() >= c2:
            winner = recursive_combat(p1.clone(c1), p2.clone(c2))
            if winner == 'p1':
                p1.add_cards(c1, c2)
            elif winner == 'p2':
                p2.add_cards(c2, c1)
            else:
                raise Exception('No one won?')
        else:
            if c1 > c2:
                p1.add_cards(c1, c2)
            elif c2 > c1:
                p2.add_cards(c2, c1)
            else:
                raise Exception('I thought this might happen')

    if not p1.empty():
        return 'p1'
    elif not p2.empty():
        return 'p2'
    else:
        raise Exception('Neither player won')


def part2(p1: Player, p2: Player):
    p1 = p1.clone()
    p2 = p2.clone()

    winner = recursive_combat(p1, p2)
    if winner == 'p1':
        print('p1 wins! Score:', p1.score())
    elif winner == 'p2':
        print('p2 wins! Score:', p2.score())


def main():
    f = open('inputs/day22.txt')
    all_text = f.read().strip()
    p1_text, p2_text = all_text.split('\n\n')
    p1 = Player([int(x) for x in p1_text.split('\n')[1:]])
    p2 = Player([int(x) for x in p2_text.split('\n')[1:]])

    # part1(p1, p2)
    part2(p1, p2)


if __name__ == "__main__":
    main()
