import os
import pathlib


def part_one():
    fully_contained_pairs = 0
    input_filename = pathlib.Path(os.path.join(os.getcwd(), 'input.txt'))
    with input_filename.open('r') as fp:
        for line in fp.readlines():
            p1, p2 = line[:-1].split(',')
            p1 = [int(x) for x in p1.split('-')]
            p2 = [int(x) for x in p2.split('-')]

            # Check if first pair is contained in second pair.
            if p1[0] >= p2[0] and p1[1] <= p2[1]:
                fully_contained_pairs += 1
                continue

            # Check if second pair is contained in first pair.
            if p2[0] >= p1[0] and p2[1] <= p1[1]:
                fully_contained_pairs += 1
                continue

    print('Pairs: ', fully_contained_pairs)


def part_two():
    fully_contained_pairs = 0
    input_filename = pathlib.Path(os.path.join(os.getcwd(), 'input.txt'))
    with input_filename.open('r') as fp:
        for line in fp.readlines():
            p1, p2 = line[:-1].split(',')
            p1 = [int(x) for x in p1.split('-')]
            p2 = [int(x) for x in p2.split('-')]

            s = set([i for i in range(p1[0], p1[1]+1)]).intersection(set([i for i in range(p2[0], p2[1]+1)]))
            if len(s) > 0:
                fully_contained_pairs += 1

    print('Pairs: ', fully_contained_pairs)


if __name__ == '__main__':
    part_one()
    part_two()
