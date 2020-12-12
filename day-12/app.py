def determine_direction(turn: str, angle: int, current_dir: str):
    """
    Turn the boat n number of times
    :param turn:
    :param angle:
    :param current_dir:
    :returns: New direction
    """
    #              0    1    2    3
    directions = ["N", "E", "S", "W"]
    num_turns = int(angle / 90)
    index = directions.index(current_dir)
    new_direction = ""

    if turn == "R":
        if num_turns + index >= len(directions):
            new_direction = directions[(num_turns + index) % len(directions)]
        else:
            new_direction = directions[num_turns + index]

    if turn == "L":
        if index - num_turns >= 0:
            new_direction = directions[index - num_turns]
        else:
            new_direction = directions[(index - num_turns) + len(directions)]

    return new_direction


if __name__ == "__main__":

    # Assert determine_direction() does what it's supposed to do
    try:
        assert determine_direction("R", 90, "N") == "E"
        assert determine_direction("L", 270, "E") == "S"
        assert determine_direction("R", 180, "S") == "N"
        assert determine_direction("L", 90, "W") == "S"
        assert determine_direction("R", 180, "N") == "S"
        assert determine_direction("L", 270, "N") == "E"
        assert determine_direction("R", 180, "E") == "W"
        assert determine_direction("L", 180, "S") == "N"
    except (AssertionError, KeyError):
        exit("Tests failed.")

    # Part 1
    input_file = open("input.txt", "r")
    instructions = input_file.read().split("\n")

    # Boat starts in this direction/position
    current_direction = "E"
    north = 0
    east = 0

    for instruction in instructions:

        direction = instruction[:1]
        movement = int(instruction[1:])

        if direction == "R" or direction == "L":
            current_direction = determine_direction(direction, movement, current_direction)

        if direction == "F":
            direction = current_direction

        if direction == "N":
            north = north + movement

        if direction == "E":
            east = east + movement

        if direction == "S":
            north = north - movement

        if direction == "W":
            east = east - movement

    # Summary
    print(("West" if east < 1 else "East") + f": {abs(east)}")
    print(("South" if north < 1 else "North") + f": {abs(north)}")
    print(f"Manhattan distance: {abs(east) + abs(north)}")

    """
    Part 2
    https://adventofcode.com/2020/day/12#part2
    ... to be continued ...
    """
