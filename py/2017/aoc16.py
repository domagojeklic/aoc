import re

def load_instructions(filename):
    with open(filename) as f:
        return f.read().split(',')

def generate_programs(num):
    return [chr(c) for c in range(ord('a'), ord('a') + num)]

def perform_instructions(programs, instructions):
    regex = re.compile('([a-z])([a-z0-9]+)(\/([a-z0-9]+))*')
    for i in instructions:
        (inst, o1, _, o2) = regex.search(i).groups()
        if inst == 's':
            programs = spin(programs, int(o1))
        elif inst == 'x':
            swap(programs, int(o1), int(o2))
        elif inst == 'p':
            partner(programs, o1, o2)
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
    instructions = load_instructions('input16.txt')
    programs = generate_programs(16)
    programs = perform_instructions(programs, instructions)
    print(''.join(programs))