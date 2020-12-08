import re

def parse_input():
    bagRules = []

    with open("input.txt") as input:
        line = input.readline()
        currentBag = {}
        while line:
            currentBag['name'] = line.split(" bag")[0]
            currentBagRuleStringSearch = re.search('contain (\d{1}[\d\w," "]+).', line)
            currentBag['rules'] = []
            if currentBagRuleStringSearch is not None:
                currentBagRuleString = currentBagRuleStringSearch.group(1)
                currentBagRules = currentBagRuleString.split(", ")
                for rule in currentBagRules:
                    formattedRule = {}
                    formattedRule['amount'] = int(rule[0])
                    ruleBagNameSearch = re.search('([a-z" "]+) bag', rule)
                    formattedRule['name'] = ruleBagNameSearch.group(1).strip()
                    currentBag['rules'].append(formattedRule)

            bagRules.append(currentBag)
            currentBag = {}
            line = input.readline()

    return bagRules


def get_number_of_bags_containing(bagName, bagsWithRules, bagsAlreadyCounted=[]):
    bagsAddedAtThisStage = []

    for bag in bagsWithRules:
        bagsAllowedInside = list(map(lambda b: b['name'], bag['rules']))
        if bagName in bagsAllowedInside and bag['name'] not in bagsAlreadyCounted:
            bagsAddedAtThisStage.append(bag['name'])
            bagsAlreadyCounted.append(bag['name'])

    return len(bagsAddedAtThisStage) + sum(map(
        lambda name: get_number_of_bags_containing(name, bagsWithRules, bagsAlreadyCounted), bagsAddedAtThisStage
    ))


def get_number_of_bags_inside(bagName, bagsWithRules, isCountingSelf=False):
    total = 1 if isCountingSelf else 0

    currentBag = [b for b in bagsWithRules if b['name'] == bagName][0]
    return total + sum(map(
        lambda rule: get_number_of_bags_inside(rule['name'], bagsWithRules, True) * rule['amount'],
        currentBag['rules']
    ))


def solve_part_one():
    bagsWithRules = parse_input()

    solution = get_number_of_bags_containing('shiny gold', bagsWithRules)
    print("The answer for part 1 is: {}".format(solution))


def solve_part_two():
    bagsWithRules = parse_input()

    solution = get_number_of_bags_inside('shiny gold', bagsWithRules)
    print("The answer for part 2 is: {}".format(solution))


if __name__ == '__main__':
    solve_part_one()
    solve_part_two()
