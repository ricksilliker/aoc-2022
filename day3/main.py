import os
import pathlib


def part_one():
    priorities = 'abcdefghijklmnopqrstuvwxyz'
    priorities += priorities.upper()

    total_priority = 0

    input_filename = pathlib.Path(os.path.join(os.getcwd(), 'input.txt'))
    with input_filename.open('r') as fp:
        for line in fp.readlines():
            rucksack_size = len(line[:-1])
            compartment_size = int(rucksack_size/2)
            c1 = line[:compartment_size]
            c2 = line[compartment_size:rucksack_size]
            common_item = list(set(c1).intersection(set(c2)))[0]
            total_priority += priorities.index(common_item)+1

    print('Total Priority: ', total_priority)


def part_two():
    priorities = 'abcdefghijklmnopqrstuvwxyz'
    priorities += priorities.upper()

    total_priority = 0

    groups = []
    current_group_size = 0
    input_filename = pathlib.Path(os.path.join(os.getcwd(), 'input.txt'))
    with input_filename.open('r') as fp:
        lines = fp.read().splitlines()
        for i in range(0, len(lines), 3):
            common_item = set.intersection(*map(set, lines[i:i+3]))
            print(lines[i:i+3], common_item)
            total_priority += priorities.index(list(common_item)[0]) + 1

    print('Total Priority: ', total_priority)


if __name__ == '__main__':
    part_one()
    part_two()
