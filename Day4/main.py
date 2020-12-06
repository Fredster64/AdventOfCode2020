import re

def get_passports_from_input():
    passports = []

    with open("input.txt") as input:
        line = input.readline()
        currentPassport = ""
        while line:
            if line == "\n":
                passports.append(convert_string_to_passport(currentPassport))
                currentPassport = ""
            else:
                currentPassport += line.strip() + " "
            line = input.readline()
        passports.append(convert_string_to_passport(currentPassport))

    return passports


def convert_string_to_passport(passportString):
    passport = {}
    passportProperties = passportString.rstrip().split(" ")

    for property in passportProperties:
        propertyInfo = re.search('(\w{3}):(.*)', property)
        passport[propertyInfo.group(1)] = propertyInfo.group(2)

    return passport


def all_required_fields_present(passport):
    numberOfEntries = len(passport)
    containsCountryID = "cid" in list(passport.keys())

    return numberOfEntries == 8 or (numberOfEntries == 7 and not containsCountryID)


def all_required_fields_present_and_valid(passport):
    validEyeColours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if not all_required_fields_present(passport):
        return False

    for key in list(passport.keys()):
        value = passport[key]

        if key == 'byr':
            if int(value) < 1920 or int(value) > 2002:
                return False
        elif key == 'iyr':
            if int(value) < 2010 or int(value) > 2020:
                return False
        elif key == 'eyr':
            if int(value) < 2020 or int(value) > 2030:
                return False
        elif key == 'hgt':
            heightInfo = re.search('(\d+)(\w{2})', value)
            heightValue = int(heightInfo.group(1))
            if heightInfo.group(2) == 'cm':
                if heightValue < 150 or heightValue > 193:
                    return False
            elif heightValue < 59 or heightValue > 76:
                return False
        elif key == 'hcl':
            hairColourInfo = re.search('#([0-9a-f]{6})', value)
            if hairColourInfo is None or len(value) != 7:
                return False
        elif key == 'ecl':
            if value not in validEyeColours:
                return False
        elif key == 'pid':
            passportIdInfo = re.search('(\d{9})', value)
            if passportIdInfo is None or len(value) > 9:
                return False

    return True

def solve_part_one():
    passports = get_passports_from_input()
    validPassports = list(filter(all_required_fields_present, passports))
    print("The answer for part 1 is: {}".format(len(validPassports)))


def solve_part_two():
    passports = get_passports_from_input()
    validPassports = list(filter(all_required_fields_present_and_valid, passports))
    print("The answer for part 2 is: {}".format(len(validPassports)))


if __name__ == '__main__':
    solve_part_one()
    solve_part_two()

