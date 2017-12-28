def perform_insertions(buffer, num_steps, num_times):
    index = 0
    for i in range(1, num_times + 1):
        index = (index + num_steps) % len(buffer) + 1
        buffer.insert(index, i)
    return index

if __name__ == '__main__':
    num_steps = 324
    num_times = 2017
    buffer = [0]
    index = perform_insertions(buffer, num_steps, num_times)
    print(buffer[index + 1])