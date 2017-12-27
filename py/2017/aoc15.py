def next_value(initial, factor, divider, multiple_of = None):
    while True:
        value = initial * factor % divider
        if multiple_of == None or value % multiple_of == 0: 
            yield value
        initial = value

def match_count(gen_a, gen_b, count):
    num_match = 0
    mask = int('1' * 16, 2)
    for _ in range(count):
        a = next(gen_a) & mask
        b = next(gen_b) & mask
        if a == b:
            num_match += 1
    return num_match
        
if __name__ == '__main__':
    part1_count = 40 * 10 ** 6
    part2_count = 5 * 10 ** 6
    factor_a = 16807
    factor_b = 48271
    starting_a_test = 65
    starting_b_test = 8921
    starting_a = 703
    starting_b = 516
    divider = 2147483647
    multiple_a = 4
    multiple_b = 8

    gen_a = next_value(starting_a, factor_a, divider)
    gen_b = next_value(starting_b, factor_b, divider)
    print('Result part 1: {0}'.format(match_count(gen_a, gen_b, part1_count)))

    gen_a_part2 = next_value(starting_a, factor_a, divider, multiple_a)
    gen_b_part2 = next_value(starting_b, factor_b, divider, multiple_b)
    print('Result part 2: {0}'.format(match_count(gen_a_part2, gen_b_part2, part2_count)))
