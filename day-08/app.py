def update_accumulator(o: str, v: int, a: int):
    """
    :param o: Operation
    :param v: Value
    :param a: Accumulator value
    :returns:  a = a [+/-] v
    """

    if o == "+":
        a += v
    elif o == "-":
        a -= v

    return a


if __name__ == "__main__":

    input_file = open("input.txt", "r")
    instructions = input_file.read().split("\n")

    n = 1
    accumulator = 0
    instruction_audit = []

    while n <= len(instructions):

        instruction = instructions[n - 1]
        action = instruction[:3]
        operation = instruction[4]
        number = instruction[5:len(instruction)]
        move = 0

        # Duplicate instruction/line. Infinite loop. Terminate.
        instruction_audit.append(n)
        if instruction_audit.count(n) > 1:
            print(f"-- Duplicate instruction! Instruction: {instruction}. Line: {n}. Accumulator: {accumulator}. --")
            break

        if action == "acc":
            accumulator = update_accumulator(operation, int(number), accumulator)
            move = 1
        elif action == "jmp":
            move = int(operation + number)
        elif action == "nop":
            move = 1

        print(f"Instruction: {instruction}, accumulator: {accumulator}, line: {n}")
        n += move

    """
    Part 2
    Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp.
    https://adventofcode.com/2020/day/8#part2
    ... to be continued ...
    """
