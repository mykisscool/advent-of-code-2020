from functools import reduce

if __name__ == "__main__":

    input_file = open("input.txt", "r")
    groups = input_file.read().split("\n\n")

    sum_unique_responses = 0  # Part 1
    sum_same_responses = 0  # Part 2

    for n, group in enumerate(groups, 1):

        group_responses = group.split("\n")
        responses_per_group = []  # Part 1
        group_response_list = []  # Part 2

        for person_responses in group_responses:

            for response in person_responses:
                responses_per_group.append(response)  # Part 1

            group_response_list.append(set(person_responses))  # Part 2

        # Part 1
        unique_responses_per_group = set(responses_per_group)
        sum_unique_responses += len(unique_responses_per_group)

        # Part 2
        same_responses_per_group = reduce(lambda x, y: x & y, group_response_list)
        sum_same_responses += len(same_responses_per_group)

        print(f"Group {n} unique responses ({len(unique_responses_per_group)}): {unique_responses_per_group}")
        print(f"Group {n} same responses ({len(same_responses_per_group)}): {same_responses_per_group}")

    print(f"Sum of unique responses: {sum_unique_responses}")
    print(f"Sum of same responses: {sum_same_responses}")
