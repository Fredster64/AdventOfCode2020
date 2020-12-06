def get_map_from_input():
    mapRanks = []

    with open("input.txt") as input:
        line = input.readline()
        while line:
            mapRanks.append(line.strip())
            line = input.readline()

    return mapRanks


def get_number_of_trees(map, movementRule):
    mapWidth = len(map[0])
    mapHeight = len(map)

    treeCount = 0
    currentYPosition = movementRule['down']
    currentXPosition = movementRule['right']
    while currentYPosition < mapHeight:
        if map[currentYPosition][currentXPosition] == '#':
            treeCount += 1

        currentYPosition += movementRule['down']
        currentXPosition = (currentXPosition + movementRule['right']) % mapWidth

    return treeCount


def solve_part_one():
    map = get_map_from_input()
    movementRule = {'right': 3, 'down': 1}
    print("The answer for part 1 is: {}".format(get_number_of_trees(map, movementRule)))


def solve_part_two():
    map = get_map_from_input()
    movementRules = [
        {'right': 3, 'down': 1},
        {'right': 1, 'down': 1},
        {'right': 5, 'down': 1},
        {'right': 7, 'down': 1},
        {'right': 1, 'down': 2}
    ]

    solution = 1
    for rule in movementRules:
        solution *= get_number_of_trees(map, rule)

    print("The answer for part 2 is: {}".format(solution))


if __name__ == '__main__':
    solve_part_one()
    solve_part_two()

