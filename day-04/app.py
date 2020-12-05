import re

REQUIRED_FIELDS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # cid is optional
EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def has_n_digits(test_num: str, desired_length: int):
    """
    :param test_num:
    :param desired_length:
    :returns: True if number is a desired length, False if it isn't
    """

    return True if len(test_num) == desired_length else False


def is_between(test_num: str, num1: int, num2: int):
    """
    :param test_num:
    :param num1:
    :param num2:
    :returns: True if number is between a desired range, False if it isn't
    """

    return True if int(test_num) in range(num1, num2 + 1) else False


def field_validator(pair: list):
    """
    Evaluates a list key/value pair and validates value based on key type
    :param pair:
    :returns: True if value is valid; False if it isn't
    """

    is_valid = True  # In case cid is passed in

    if pair[0] == "byr":
        is_valid = True if has_n_digits(pair[1], 4) and is_between(pair[1], 1920, 2002) else False

    if pair[0] == "iyr":
        is_valid = True if has_n_digits(pair[1], 4) and is_between(pair[1], 2010, 2020) else False

    if pair[0] == "eyr":
        is_valid = True if has_n_digits(pair[1], 4) and is_between(pair[1], 2020, 2030) else False

    if pair[0] == "hgt":
        measurement = pair[1][-2:]
        if measurement == "cm":
            is_valid = True if is_between(pair[1][:-2], 150, 193) else False
        elif measurement == "in":
            is_valid = True if is_between(pair[1][:-2], 59, 76) else False
        else:
            is_valid = False

    if pair[0] == "hcl":
        is_valid = True if re.search(r"^#(?:[0-9a-fA-F]{3}){1,2}$", pair[1]) else False

    if pair[0] == "ecl":
        is_valid = True if pair[1] in EYE_COLORS else False

    if pair[0] == "pid":
        is_valid = True if has_n_digits(pair[1], 9) else False

    return is_valid


if __name__ == "__main__":

    input_file = open("input.txt", "r")
    lines = input_file.read().split("\n\n")
    good_passports = []

    # Part 1
    for line in lines:
        matched = 0
        for field in REQUIRED_FIELDS:
            if field + ":" in line:
                matched += 1

        if matched == len(REQUIRED_FIELDS):
            good_passports.append(line)

    print(f"Total passports: {len(lines)}\nComplete passports: {len(good_passports)}")

    # Part 2
    good_and_valid_passports = 0
    for good_passport in good_passports:
        split_fields = re.split("[\n ]", good_passport)

        field_valid_list = []
        for split_field in split_fields:
            key_and_value = split_field.split(":")
            is_field_valid = field_validator(key_and_value)
            field_valid_list.append(is_field_valid)

        if all(field_valid_list):
            good_and_valid_passports += 1

    print(f"Valid passports: {good_and_valid_passports}")
