ROWS = 128
COLS = 8
ROW_RANGE = range(0, ROWS)
COL_RANGE = range(0, COLS)


def get_boarding_pass_id(seat: dict):
    """
    :param seat:
    :returns: A unique id based on seat location
    """

    return seat["row"] * 8 + seat["col"]


def parse_boarding_pass(boarding: str):
    """
    :param boarding:
    :returns: A dictionary containing row and column
    """

    temp_row_range = ROW_RANGE
    temp_col_range = COL_RANGE

    for letter in boarding[0:6]:
        if letter == "F":
            temp_row_range = temp_row_range[:len(temp_row_range) // 2]
        elif letter == "B":
            temp_row_range = temp_row_range[len(temp_row_range) // 2:]

    for letter in boarding[7:9]:
        if letter == "L":
            temp_col_range = temp_col_range[:len(temp_col_range) // 2]
        elif letter == "R":
            temp_col_range = temp_col_range[len(temp_col_range) // 2:]

    return {
        "row": temp_row_range[0] if boarding_pass[6] == "F" else temp_row_range[-1],
        "col": temp_col_range[0] if boarding_pass[9] == "L" else temp_col_range[-1]
    }


if __name__ == "__main__":

    input_file = open("input.txt", "r")
    passes = input_file.read().split("\n")
    unique_ids = []
    find_missing_pass = {}

    # Part 1
    for boarding_pass in passes:
        parsed_boarding_pass = parse_boarding_pass(boarding_pass)
        unique_ids.append(get_boarding_pass_id(parsed_boarding_pass))

        # Create a dictionary of lists for part 2
        try:
            find_missing_pass[parsed_boarding_pass["row"]].append(parsed_boarding_pass["col"])
        except KeyError:
            find_missing_pass[parsed_boarding_pass["row"]] = [parsed_boarding_pass["col"]]

    print(f"Highest unique ID: {max(unique_ids)}")

    # Part 2
    rows_to_inspect = {}
    for row in find_missing_pass:
        num_seats_in_row = len(find_missing_pass[row])
        if num_seats_in_row != COLS:
            rows_to_inspect[row] = find_missing_pass[row]

    open_seats = {}
    for row in rows_to_inspect:
        temp_open_seats = []
        for n in COL_RANGE:
            if n not in rows_to_inspect[row]:
                temp_open_seats.append(n)

            open_seats[row] = temp_open_seats

    print("\nPotential open seats:")
    for row in open_seats:
        for seat in open_seats[row]:
            print(f"Row: {row}, Seat: {seat}, ID: {get_boarding_pass_id({'row': row, 'col': seat})}")
