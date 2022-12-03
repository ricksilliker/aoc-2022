import os
import pathlib


def part_one():
    lose_bonus = 0
    draw_bonus = 3
    win_bonus = 6

    strategy_key = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    total_score = 0

    input_filename = pathlib.Path(os.path.join(os.getcwd(), 'input.txt'))
    with input_filename.open('r') as fp:
        for line in fp.readlines():
            a, b = line[:-1].split(' ')
            a = strategy_key[a]
            b = strategy_key[b]

            # draw
            if a == b:
                total_score += draw_bonus + b
                continue
            # rock vs scissor
            if a + 2 == b:
                total_score += lose_bonus + b
                continue
            # scissor vs rock
            if a == b + 2:
                total_score += win_bonus + b
                continue
            # scissor vs paper and papper vs rock
            if a > b:
                total_score += lose_bonus + b
                continue

            total_score += win_bonus + b

    print('Total Score: ', total_score)


def part_two():
    lose_bonus = 0
    draw_bonus = 3
    win_bonus = 6

    strategy_key = {
        'A': {'X': 3+lose_bonus, 'Y': 1+draw_bonus, 'Z': 2+win_bonus},
        'B': {'X': 1+lose_bonus, 'Y': 2+draw_bonus, 'Z': 3+win_bonus},
        'C': {'X': 2+lose_bonus, 'Y': 3+draw_bonus, 'Z': 1+win_bonus}
    }

    total_score = 0

    input_filename = pathlib.Path(os.path.join(os.getcwd(), 'input.txt'))
    with input_filename.open('r') as fp:
        for line in fp.readlines():
            a, b = line[:-1].split(' ')
            total_score += strategy_key[a][b]

    print('Total Score: ', total_score)


if __name__ == '__main__':
    part_one()
    part_two()
    