import re

def get_password_array_from_input():
    passwordArray = []

    with open("input.txt") as input:
        line = input.readline()
        while line:
            passwordArray.append(line.strip())
            line = input.readline()

    return passwordArray

def isPasswordValidForPartOne(password):
    passwordInfo = re.search('(\d{1,2})-(\d{1,2}) (\w{1}): (\w+)', password)
    minOccurrences = int(passwordInfo.group(1))
    maxOccurrences = int(passwordInfo.group(2))
    characterToCheck = passwordInfo.group(3)
    passwordString = passwordInfo.group(4)

    numberOfOccurrences = passwordString.count(characterToCheck)
    return numberOfOccurrences >= minOccurrences and numberOfOccurrences <= maxOccurrences

def solve_part_one():
    passwordArray = get_password_array_from_input()
    validPasswordArray = list(filter(isPasswordValidForPartOne, passwordArray))
    print("The answer for part 1 is: {}".format(len(validPasswordArray)))

def isPasswordValidForPartTwo(password):
    passwordInfo = re.search('(\d{1,2})-(\d{1,2}) (\w{1}): (\w+)', password)
    firstPosition = int(passwordInfo.group(1)) - 1
    secondPosition = int(passwordInfo.group(2)) - 1
    characterToCheck = passwordInfo.group(3)
    passwordString = passwordInfo.group(4)

    firstPositionIsCheckedCharacter = passwordString[firstPosition] == characterToCheck
    secondPositionIsCheckedCharacter = passwordString[secondPosition] == characterToCheck

    return firstPositionIsCheckedCharacter != secondPositionIsCheckedCharacter

def solve_part_two():
    passwordArray = get_password_array_from_input()
    validPasswordArray = list(filter(isPasswordValidForPartTwo, passwordArray))
    print("The answer for part 2 is: {}".format(len(validPasswordArray)))

if __name__ == '__main__':
    solve_part_one()
    solve_part_two()

