import re

if __name__ == "__main__":

    input_file = open("input.txt", "r")
    lines = input_file.read().split("\n")

    """
    Creates a set that reads: "key can fit inside associative set".
    """
    set_containers = {}
    set_containers_2 = {}  # Part 2

    for line in lines:

        # Simplify string (kind of ugly - strip out unwanted words and punctuation)
        simple = line.replace(" bags contain", "-").replace(".", "").replace(",", "").replace("bags", "-") \
            .replace("bag", "-").rstrip("-")

        # Part 2
        hierarchy_2 = [x.strip() for x in simple.split("-")]

        # Part 1
        simple = re.sub("[0-9]", "", simple)
        hierarchy = [x.strip() for x in simple.split("-")]

        for i, color in enumerate(hierarchy):
            if i == 0:
                continue

            try:
                set_containers[color].add(hierarchy[0])
            except KeyError:
                set_containers[color] = {hierarchy[0]}

        # Part 2
        set_containers_2[hierarchy_2.pop(0)] = hierarchy_2

    """
    (Part 1) Finds bag colors recursively
    """
    def check_bags(subset: set):
        bags = set()

        for bag_color in subset:
            try:
                bags |= set_containers[bag_color]
            except KeyError:
                pass

        merged = bags.union(subset)

        if len(merged) == len(subset):
            return merged
        else:
            return check_bags(merged)

    starting_bag = set_containers["shiny gold"]
    all_bags = check_bags(starting_bag)

    print(f"Bags that can contain \"shiny gold\" ({len(all_bags)}):\n{sorted(all_bags)}")

    """
    (Part 2) Find the number of bags recursively
    https://adventofcode.com/2020/day/7#part2
    ... to be continued ...
    """
