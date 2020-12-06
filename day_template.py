def parse_input():
    returnObject = []

    with open("input.txt") as input:
        line = input.readline()
        while line:
            returnObject.append(line.strip())
            line = input.readline()

    return returnObject

def solve_part_one():
    inputObject = parse_input()
    print("The answer for part 1 is: {}".format(inputObject))

def solve_part_two():
    inputObject = parse_input()
    print("The answer for part 2 is: {}".format(inputObject))

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()