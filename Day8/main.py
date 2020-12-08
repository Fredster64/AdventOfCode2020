import copy

def parse_input():
    gameInstructions = []

    with open("input.txt") as input:
        line = input.readline()
        instruction = {}
        index = 0
        while line:
            lineSplit = line.split(" ")
            instruction['operation'] = lineSplit[0]
            instruction['argument'] = int(lineSplit[1])
            instruction['index'] = index
            gameInstructions.append(instruction)

            instruction = {}
            index += 1
            line = input.readline()

    return gameInstructions


def get_accumulator_change(instruction):
    if instruction['operation'] != 'acc':
        return 0

    return instruction['argument']


def get_index_change(instruction):
    if instruction['operation'] != 'jmp':
        return 1

    return instruction['argument']


def get_accumulator_before_first_repeat(gameInstructions):
    instructionIndicesAlreadyVisited = []
    currentInstructionIndex = 0
    accumulator = 0

    while currentInstructionIndex not in instructionIndicesAlreadyVisited:
        instructionIndicesAlreadyVisited.append(currentInstructionIndex)
        currentInstruction = gameInstructions[currentInstructionIndex]

        accumulator += get_accumulator_change(currentInstruction)
        currentInstructionIndex += get_index_change(currentInstruction)

    return accumulator


def fix_program(gameInstructions):
    currentIndex = 0
    tempGameInstructions = copy.deepcopy(gameInstructions)
    while True:
        if gameInstructions[currentIndex]['operation'] != 'acc':
            if gameInstructions[currentIndex]['operation'] == 'nop':

                tempGameInstructions[currentIndex]['operation'] = 'jmp'
            else:
                tempGameInstructions[currentIndex]['operation'] = 'nop'

            tempFinalAccumulator = get_final_accumulator(tempGameInstructions)
            if tempFinalAccumulator is not None:
                return tempFinalAccumulator

        tempGameInstructions = copy.deepcopy(gameInstructions)
        currentIndex += 1


def get_final_accumulator(gameInstructions):
    accumulator = 0
    currentIndex = 0
    indicesAlreadyVisited = []
    
    while currentIndex < len(gameInstructions):
        if currentIndex in indicesAlreadyVisited: 
            return None
        
        indicesAlreadyVisited.append(currentIndex)
        currentInstruction = gameInstructions[currentIndex]

        accumulator += get_accumulator_change(currentInstruction)
        currentIndex += get_index_change(currentInstruction)
        
    return accumulator


def solve_part_one():
    gameInstructions = parse_input()

    solution = get_accumulator_before_first_repeat(gameInstructions)
    print("The answer for part 1 is: {}".format(solution))


def solve_part_two():
    gameInstructions = parse_input()

    solution = fix_program(gameInstructions)
    print("The answer for part 2 is: {}".format(solution))


if __name__ == '__main__':
    solve_part_one()
    solve_part_two()
