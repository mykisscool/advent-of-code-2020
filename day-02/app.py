def parse_rule_1(rule: str):
    """
    Must contain a specified character n times
    :param rule:
    :returns: True for a valid password, False for an invalid password
    """

    rule_segments = rule.replace(":", "").split(" ")
    occurrences = rule_segments[0].split("-")
    range_occurrences = range(int(occurrences[0]), int(occurrences[1]) + 1)
    letter = rule_segments[1]
    password = rule_segments[2]
    letter_occurrences = password.count(letter)

    return True if letter_occurrences in range_occurrences else False


def parse_rule_2(rule: str):
    """
    Must contain a specified character at certain indexes
    :param rule:
    :returns: True for a valid password, False for an invalid password
    """

    rule_segments = rule.replace(":", "").split(" ")
    positions = rule_segments[0].split("-")
    position_1 = int(positions[0])
    position_2 = int(positions[1])
    letter = rule_segments[1]
    password = rule_segments[2]

    return True if (password[position_1 - 1] == letter) ^ (password[position_2 - 1] == letter) else False


if __name__ == "__main__":

    input_file = open("input.txt", "r")
    lines = input_file.read().split("\n")
    good_passwords_rule_1 = 0
    good_passwords_rule_2 = 0

    for line in lines:
        good_passwords_rule_1 += 1 if parse_rule_1(line) else 0
        good_passwords_rule_2 += 1 if parse_rule_2(line) else 0

    print(f"Valid passwords for rule 1: {good_passwords_rule_1}.")
    print(f"Valid passwords for rule 2: {good_passwords_rule_2}.")
