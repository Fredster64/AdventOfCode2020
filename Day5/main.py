def parse_input():
    boardingPasses = []

    with open("input.txt") as input:
        line = input.readline()
        while line:
            boardingPasses.append(line.strip())
            line = input.readline()

    return boardingPasses


def get_seat_ID(boardingPass):
    return 8 * get_row(boardingPass) + get_column(boardingPass)


def get_row(boardingPass):
    rowNumber = 0
    currentIndex = 0
    while currentIndex < 7:
        if boardingPass[currentIndex] == 'B':
            rowNumber += 2 ** (6 - currentIndex)
        currentIndex += 1

    return rowNumber


def get_column(boardingPass):
    columnNumber = 0
    currentIndex = 7
    while currentIndex < 10:
        if boardingPass[currentIndex] == 'R':
            columnNumber += 2 ** (9 - currentIndex)
        currentIndex += 1

    return columnNumber


def get_boarding_pass_from_seat_id(seatID):
    columnString = ""
    columnNumber = seatID % 8
    amountLeftToAdd = columnNumber
    binaryPosition = 2
    while binaryPosition >= 0:
        if amountLeftToAdd >= 2 ** binaryPosition:
            amountLeftToAdd -= 2 ** binaryPosition
            columnString += "R"
        else:
            columnString += "L"
        binaryPosition -= 1

    rowString = ""
    rowNumber = (seatID - columnNumber) / 8
    amountLeftToAdd = rowNumber
    binaryPosition = 6
    while binaryPosition >= 0:
        if amountLeftToAdd >= 2 ** binaryPosition:
            amountLeftToAdd -= 2 ** binaryPosition
            rowString += "B"
        else:
            rowString += "F"
        binaryPosition -= 1

    return rowString + columnString

def solve_part_one():
    boardingPasses = parse_input()
    boardingPassIDs = map(get_seat_ID, boardingPasses)
    solution = max(boardingPassIDs)
    print("The answer for part 1 is: {}".format(solution))
    return solution


def solve_part_two(maxSeatID):
    boardingPasses = parse_input()
    checkedSeatID = maxSeatID - 1
    while True:
        if get_boarding_pass_from_seat_id(checkedSeatID) not in boardingPasses:
            print("The answer for part 2 is: {}".format(checkedSeatID))
            return
        checkedSeatID -= 1


if __name__ == '__main__':
    partOneSolution = solve_part_one()
    solve_part_two(partOneSolution)