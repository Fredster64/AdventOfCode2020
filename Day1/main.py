def get_expense_report_from_input():
    expenseReportAsArray = []

    with open("input.txt") as input:
        line = input.readline()
        while line:
            expenseReportAsArray.append(int(line.strip()))
            line = input.readline()

    return expenseReportAsArray

def solve_part_two():
    expenseReport = get_expense_report_from_input()
    expenseReport.sort()

    indexOfCheckedEntry = 0
    while indexOfCheckedEntry < len(expenseReport):
        checkedEntry = expenseReport[indexOfCheckedEntry]

        secondEntryIndex = indexOfCheckedEntry
        while checkedEntry + expenseReport[secondEntryIndex] < 2020:
            secondEntry = expenseReport[secondEntryIndex]
            if 2020 - (checkedEntry + secondEntry) in expenseReport:
                print("The answer is {}".format(checkedEntry * secondEntry * (2020 - checkedEntry - secondEntry)))
                return

            secondEntryIndex += 1

        indexOfCheckedEntry += 1

    print("Couldn't find a solution")

if __name__ == '__main__':
    solve_part_two()

