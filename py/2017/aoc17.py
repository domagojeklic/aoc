def perform_insertions(buffer, num_steps, num_times):
    index = 0
    for i in range(1, num_times + 1):
        index = (index + num_steps) % len(buffer) + 1
        buffer.insert(index, i)
    return index

def num_at_first_index(num_steps, num_times):
    buff_len = 1
    index = 0
    for i in range(1, num_times + 1):
        index = (index + num_steps) % buff_len + 1
        buff_len += 1
        if index == 1: num = i
    return num

if __name__ == '__main__':
    num_steps = 324
    num_times1 = 2017
    num_times2 = 50 * 10 ** 6
    buffer = [0]
    index = perform_insertions(buffer, num_steps, num_times1)
    print('Result part 1: {0}'.format(buffer[index + 1]))
    num = num_at_first_index(num_steps, num_times2)
    print('Result part 2: {0}'.format(num))