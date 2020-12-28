def transform_subject_no(subject_no: int, loop_size: int) -> int:
    value = 1

    for _ in range(loop_size):
        value *= subject_no
        value %= 20201227

    return value


def part1(card_pub_key: int, door_pub_key: int):
    value = 1
    subject_no = 7
    for card_loop_size in range(1, 100000000):
        value *= subject_no
        value %= 20201227

        if value == card_pub_key:
            print(transform_subject_no(door_pub_key, card_loop_size))
            break


def main():
    f = open('inputs/day25.txt')

    card_pub_key = int(f.readline().strip())
    door_pub_key = int(f.readline().strip())

    part1(card_pub_key, door_pub_key)


if __name__ == "__main__":
    main()
