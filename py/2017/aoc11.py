def num_steps(x, y):
    num = 0
    x = abs(x)
    y = abs(y)

    while x != 0 and y != 0:
        num += 1
        x -= 1
        y -= 0.5
    
    if x != 0 or y != 0:
        num += x if x != 0 else y
    return int(num)

def process_input(input):
    x = 0
    y = 0

    dirArr = input.split(',')
    for direction in dirArr:
        # print(direction)
        if direction == 'n':
            y += 1
        elif direction == 'ne':
            x += 1
            y += 0.5
        elif direction == 'se':
            x += 1
            y -= 0.5
        elif direction == 's':
            y -= 1
        elif direction == 'sw':
            x -= 1
            y -= 0.5
        elif direction == 'nw':
            x -= 1
            y += 0.5
        else:
            raise AssertionError
    
    return (x, y)

def get_input(filename):
    with open(filename) as f:
        return f.read().replace(" ", "")

if __name__ == '__main__':
    input = get_input("input11.txt")
    (x, y) = process_input(input)
    print("x = {0}, y = {1}".format(x, y))
    print("Result = {0}".format(num_steps(x, y)))
