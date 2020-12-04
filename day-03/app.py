from functools import reduce

TREE = "#"
RIGHT = 3  # Part 1
ALTERING_SLOPES = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]  # Part 2

if __name__ == "__main__":

    input_file = open("input.txt", "r")
    lines = input_file.read().split("\n")
    trees_encountered = 0

    # Part 1
    for n, line in enumerate(lines):
        position = RIGHT * n + 1

        # Expand the line to accommodate the position of the slope
        while position >= len(line):
            line += line

        if line[position - 1] == TREE:
            trees_encountered += 1

    print(f"Trees encountered for slope {RIGHT}: {trees_encountered}")

    # Part 2
    different_slopes = []

    for s in ALTERING_SLOPES:
        trees_encountered = 0

        for n, line in enumerate(lines):

            # Potentially skipping lines
            if (n + s[1]) % s[1] != 0:
                continue

            position = s[0] * n + s[1]

            while position >= len(line):
                line += line

            if line[position - 1] == TREE:
                trees_encountered += 1

        print(f"Trees encountered for slope {s}: {trees_encountered}")
        different_slopes.append(trees_encountered)

    print(f"All trees encountered (multiplied): {reduce((lambda x, y: x * y), different_slopes)}")
