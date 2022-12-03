import os
import pathlib


def parse_input():
    elf_calories = [[]]
    input_filename = pathlib.Path(os.path.join(os.getcwd(), 'input.txt'))
    with input_filename.open('r') as fp:
        for line in fp.readlines():
            if line == '\n':
                elf_calories.append([])
                continue
            elf_calories[-1].append(int(line))

    return elf_calories


def part_one(elf_calories):
    most_calories = 0
    for elf in elf_calories:
        sum_calories = 0
        for cal in elf:
            sum_calories += cal
        if sum_calories > most_calories:
            most_calories = sum_calories

    print('Most Calories: ', most_calories)


def part_two(elf_calories):
    sum_calories = []
    for elf in elf_calories:
        count = 0
        for cal in elf:
            count += cal
        sum_calories.append(count)

    total_calories = 0
    for x in sorted(sum_calories)[len(sum_calories)-3:]:
        total_calories += x

    print('Most Calories: ', total_calories)


if __name__ == '__main__':
    elf_calories = parse_input()
    part_one(elf_calories)
    part_two(elf_calories)
