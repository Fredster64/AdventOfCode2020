def parse_input():
    answersByGroup = []
    group = []

    with open("input.txt") as input:
        line = input.readline()
        while line:
            if line == "\n":
                answersByGroup.append(group)
                group = []
            else:
                group.append(line.strip())

            line = input.readline()
        answersByGroup.append(group)

    return answersByGroup


def get_total_number_answered(group):
    answersFound = []
    for answerSet in group:
        for answer in answerSet:
            if answer not in answersFound:
                answersFound.append(answer)

    return len(answersFound)


def get_number_answered_by_all(group):
    wholeGroupAnswers = ""
    for answerSet in group:
        wholeGroupAnswers += answerSet

    answeredByAll = list(filter(lambda answer: wholeGroupAnswers.count(answer) == len(group), group[0]))
    return len(answeredByAll)


def solve_part_one():
    answersByGroup = parse_input()
    numberAnsweredForEachGroup = map(get_total_number_answered, answersByGroup)
    print("The answer for part 1 is: {}".format(sum(numberAnsweredForEachGroup)))


def solve_part_two():
    answersByGroup = parse_input()
    numberAnsweredForEachGroup = map(get_number_answered_by_all, answersByGroup)
    print("The answer for part 2 is: {}".format(sum(numberAnsweredForEachGroup)))


if __name__ == '__main__':
    solve_part_one()
    solve_part_two()