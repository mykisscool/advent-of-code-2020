import random
from functools import reduce

if __name__ == "__main__":

    input_file = open("input.txt", "r")
    rows = input_file.read().split("\n")

    """
    1. Create a dictionary of properties and ranges:
    {
        'property 1': [range(1, 5), range(6, 10)],
        'property 2': [range(2, 6), range(7, 12)],
    }
    
    2. Create a list representing my ticket:
    [
        10, 15, 20, 25, 30
    ]
    
    3. Create list of lists representing nearby tickets:
    [
        [1, 2, 3, 4, 5],
        [4, 5, 6, 7, 8],
    ]
    """

    ticket_properties = {}
    my_ticket = []
    nearby_tickets = []

    for n, row in enumerate(rows):
        if ":" in row and "ticket" not in row:

            string_ranges = row.split(":")[1].lstrip().split(" or ")
            int_ranges = []

            for string_range in string_ranges:

                if len(string_range):
                    range_parts = string_range.split("-")
                    int_ranges.append(range(int(range_parts[0]), int(range_parts[1]) + 1))

            ticket_properties[row.partition(":")[0]] = int_ranges

        elif "your ticket" in row:
            my_ticket = list(map(int, rows[n + 1].split(",")))

        elif "nearby tickets" in row:
            chunk = range(n + 1, len(rows))
            for i in chunk:
                nearby_tickets.append(list(map(int, rows[i].split(","))))

    # Part 1: Find all the integers in the tickets that do not fall in any range
    bad_values = []
    invalid_tickets = []

    for nearby_ticket in nearby_tickets:
        for v in nearby_ticket:
            not_in_range = 0

            for p in ticket_properties:
                if v not in ticket_properties[p][0] and v not in ticket_properties[p][1]:
                    not_in_range += 1

            if not_in_range == len(ticket_properties):
                bad_values.append(v)
                invalid_tickets.append(nearby_ticket)

    print(f"\nNumber of tickets: {len(nearby_tickets)}.")
    print(f"Number of invalid tickets: {len(bad_values)}.")
    print(f"Sum of invalid numbers: {sum(bad_values)}.")

    """
    Part 2: Find out which fields are which
    https://adventofcode.com/2020/day/16#part2
    ... to be continued ...
    """

    valid_tickets = []  # Work with valid tickets only
    for nearby_ticket in nearby_tickets:
        if nearby_ticket not in invalid_tickets:
            valid_tickets.append(nearby_ticket)

    # Convert the properties to a list so we can shuffle it
    list_ticket_properties = list(ticket_properties.values())  # Convert to a list so we can shuffle it

    """
    Shuffle the ticket properties until we get all valid tickets. Hoping to get lucky on this one ...
    """
    print("\nSearching for the right order of \"departure\" properties ...")
    iterations = 0

    while True:
        if iterations == 99999:
            exit("Too many attempts. Try again.")

        good_tickets = 0

        for ticket in valid_tickets:
            good_ranges = 0

            for i, p in enumerate(list_ticket_properties):
                if ticket[i] in p[0] or ticket[i] in p[1]:
                    good_ranges += 1

            # Good ticket
            if good_ranges == len(list_ticket_properties):
                good_tickets += 1

        # All good tickets
        if good_tickets == len(valid_tickets):
            print(f"\nTotal iterations: {iterations}!")
            print(f"Correct order of properties:")

            z = 0
            multiply_list = []

            for r in list_ticket_properties:
                for p in ticket_properties:
                    if ticket_properties[p] == r:
                        z += 1
                        if "departure" in p:
                            multiply_list.append(my_ticket[z - 1])
                            print(f"{z}.) {p}")

            print(f"\nMy ticket: {my_ticket}")
            print(f"Multiplied values: {reduce((lambda x, y: x * y), multiply_list)}")
            exit()
        else:
            iterations += 1
            random.shuffle(list_ticket_properties)
