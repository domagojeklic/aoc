from queue import Queue

msg_queue0 = Queue()
msg_queue1 = Queue()

def is_number(s):
    try:
        int(s)
    except ValueError:
        return False

    return True

def load_instructions(file):
    with open(file) as f:
        return [line.split() for line in f.read().split('\n')]

def perform_isntructions(instructions, pid):
    snd_queue = msg_queue0 if pid == 1 else msg_queue1
    rcv_queue = msg_queue0 if pid == 0 else msg_queue1
    registers_dict = {'p' : pid}
    current_inst = 0
    snd_msg_count = 0
    while current_inst >= 0 and current_inst < len(instructions):
        inst = instructions[current_inst]
        i = inst[0]
        op1 = inst[1]
        op2 = None
        if len(inst) == 3:
            op2 = inst[2]
            if is_number(op2):
                op2 = int(op2)
            else:
                op2 = registers_dict.get(op2, 0)

        if i == 'snd':
            msg = registers_dict.get(op1, 0)
            snd_queue.put(msg)
            snd_msg_count += 1
            # print('Program {0} sending message #{1}'.format(pid, snd_msg_count))
        elif i == 'set':
            registers_dict[op1] = op2
        elif i == 'add':
            registers_dict[op1] = registers_dict.get(op1, 0) + op2
        elif i == 'mul':
            registers_dict[op1] = registers_dict.get(op1, 0) * op2
        elif i == 'mod':
            registers_dict[op1] = registers_dict.get(op1, 0) % op2
        elif i == 'rcv':
            while rcv_queue.qsize() == 0:
                yield snd_msg_count
            msg = rcv_queue.get()
            registers_dict[op1] = msg
        elif i == 'jgz':
            if is_number(op1):
                value = int(op1)
            else:
                value = registers_dict.get(op1, 0)
            if value > 0:
                current_inst += op2 - 1
        
        current_inst += 1
    yield snd_msg_count

if __name__ == '__main__':
    instructions = load_instructions('input18.txt')
    waiting_msg0 = False
    waiting_msg1 = False
    prog0 = perform_isntructions(instructions, 0)
    prog1 = perform_isntructions(instructions, 1)
    prog1_count = 0

    try:
        while (not waiting_msg0 or (waiting_msg0 and msg_queue0.qsize() != 0)) or (not waiting_msg1 or (waiting_msg1 and msg_queue1.qsize() != 0)):
            active_prog = 0
            next(prog0)
            waiting_msg0 = True
            active_prog = 1
            prog1_count = next(prog1)
            waiting_msg1 = True
    except StopIteration:
        print('Program{0} finished!'.format(active_prog))
    finally:
        print('Result par2: {0}'.format(prog1_count))
