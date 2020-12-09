def parse_input():
    returnObject = []

    with open("input.txt") as input:
        line = input.readline()
        while line:
            returnObject.append(int(line.strip()))
            line = input.readline()

    return returnObject


def get_first_number_not_sum_of_two_previous_count(allNumbers, count):
    currentIndex = count

    while currentIndex < len(allNumbers):
        sumFound = False
        currentNumber = allNumbers[currentIndex]

        for firstIndex in range(count):
            if sumFound:
                continue
            firstNumber = allNumbers[currentIndex - count + firstIndex]

            for secondIndex in range(firstIndex + 1, currentIndex):
                secondNumber = allNumbers[secondIndex]
                if firstNumber + secondNumber == currentNumber:
                    sumFound = True
                    currentIndex += 1
                    break

        if not sumFound:
            return currentNumber

    return None


def find_encryption_weakness(allNumbers, count):
    invalidNumber = get_first_number_not_sum_of_two_previous_count(allNumbers, count)

    for currentIndex in range(len(allNumbers)):
        firstNumberInRange = allNumbers[currentIndex]
        rangeChecked = [firstNumberInRange]
        runningSum = firstNumberInRange
        stepsAheadOfFirstIndex = 0
        while runningSum < invalidNumber:
            stepsAheadOfFirstIndex += 1
            runningSum += allNumbers[currentIndex + stepsAheadOfFirstIndex]
            rangeChecked.append(allNumbers[currentIndex + stepsAheadOfFirstIndex])

        if runningSum == invalidNumber:
            return min(rangeChecked) + max(rangeChecked)


def solve_part_one():
    allNumbers = parse_input()

    solution = get_first_number_not_sum_of_two_previous_count(allNumbers, 25)
    print("The answer for part 1 is: {}".format(solution))


def solve_part_two():
    allNumbers = parse_input()

    solution = find_encryption_weakness(allNumbers, 25)
    print("The answer for part 2 is: {}".format(solution))


if __name__ == '__main__':
    solve_part_one()
    solve_part_two()
