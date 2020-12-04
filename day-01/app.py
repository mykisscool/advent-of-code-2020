if __name__ == "__main__":

    input_file = open("input.txt", "r")
    lines = list(map(int, input_file.read().split("\n")))

    # Part 1
    for outer_line in lines:
        for inner_line in lines:
            if outer_line + inner_line == 2020:
                print(f"Entry 1: {outer_line}\nEntry 2: {inner_line}\nMultiplied: {outer_line * inner_line}")
                break
        else:
            continue
        break

    # Part 2
    print("\n")
    for outer_line in lines:
        for middle_line in lines:
            for inner_line in lines:
                if outer_line + middle_line + inner_line == 2020:
                    print(f"Entry 1: {outer_line}\nEntry 2: {middle_line}\nEntry 3: {inner_line}"
                          f"\nMultiplied: {outer_line * middle_line * inner_line}")
                    break
            else:
                continue
            break
        else:
            continue
        break
