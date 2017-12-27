import re

def load_file(filename):
    with open(filename) as f:
        return f.read().split(',')

def generate_programs(num):
    return [chr(c) for c in range(ord('a'), ord('a') + num)]

def load_instructions(strarr):
    instructions = []
    regex = re.compile('([a-z])([a-z0-9]+)(\/([a-z0-9]+))*')
    for i in strarr:
        (inst, o1, _, o2) = regex.search(i).groups()
        if inst == 's':
            instructions.append((spin, int(o1)))
        elif inst == 'x':
            instructions.append((swap, int(o1), int(o2)))
        elif inst == 'p':
            instructions.append((partner, o1, o2))
    return instructions

def perform_instructions(programs, instructions, num = 1):
    programs_dict = {}
    for i in range(num):
        for inst_tuple in instructions:
            inst = inst_tuple[0]
            if inst == spin:
                programs = spin(programs, inst_tuple[1])
            else:
                inst(programs, inst_tuple[1], inst_tuple[2])

        key = ''.join(programs)
        if key in programs_dict:
            diff = i - programs_dict[key]
            remaining = num % diff
            return perform_instructions(programs, instructions, remaining - 1)
        else:
            programs_dict[key] = i
    return programs

def spin(programs, operand):
    return programs[-operand:] + programs[:-operand]

def swap(programs, operand1, operand2):
    programs[operand1], programs[operand2] = programs[operand2], programs[operand1]

def partner(programs, operand1, operand2):
    i1 = programs.index(operand1)
    i2 = programs.index(operand2)
    swap(programs, i1, i2)

if __name__ == '__main__':
    prog_num = 16
    instructions_strings = load_file('input16.txt')
    programs = generate_programs(prog_num)
    instructions = load_instructions(instructions_strings)
    result1 = ''.join(perform_instructions(programs, instructions))
    print('Result part 1: {0}'.format(result1))
    programs = generate_programs(prog_num)
    result2 = ''.join(perform_instructions(programs, instructions, 10 ** 9))
    print('Result part 2: {0}'.format(result2))