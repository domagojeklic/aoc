def load_instructions(file):
    with open(file) as f:
        return [line.split() for line in f.read().split('\n')]

def perform_isntructions(instructions):
    frequency = 0
    registers_dict = {}
    current_inst = 0
    while current_inst >= 0 and current_inst < len(instructions):
        inst = instructions[current_inst]
        i = inst[0]
        op1 = inst[1]
        op2 = None
        if len(inst) == 3:
            op2 = inst[2]
            if op2.lstrip('-').isdigit():
                op2 = int(op2)
            else:
                op2 = registers_dict.get(op2, 0)
        if i == 'snd':
            if op1.isdigit():
                frequency = int(op1)
            else:
                frequency = registers_dict.get(op1, 0)
        elif i == 'set':
            registers_dict[op1] = op2
        elif i == 'add':
            registers_dict[op1] = registers_dict.get(op1, 0) + op2
        elif i == 'mul':
            registers_dict[op1] = registers_dict.get(op1, 0) * op2
        elif i == 'mod':
            registers_dict[op1] = registers_dict.get(op1, 0) % op2
        elif i == 'rcv':
            if registers_dict.get(op1, 0) != 0:
                registers_dict[op1] = frequency
                return frequency
        elif i == 'jgz':
            if registers_dict.get(op1, 0) != 0:
                current_inst += op2 - 1
        
        current_inst += 1
            
            
    

if __name__ == '__main__':
    instructions = load_instructions('input18.txt')
    frequency = perform_isntructions(instructions)
    print(frequency)