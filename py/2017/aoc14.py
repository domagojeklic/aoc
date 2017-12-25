from aoc10 import knot_hash

def num_ones(input):
    count = 0
    for c in input:
        if c == '1':
            count += 1
    return count

def num_squares(input):
    num = 0
    for i in range(128):
        hash = knot_hash('{0}-{1}'.format(input, i))
        bin_row = bin(int(hash, 16))[2:].zfill(128)
        num += bin_row.count('1')
    return num

if __name__ == '__main__':
    input = 'nbysizxe'
    print('Result part 1: {0}'.format(num_squares(input)))