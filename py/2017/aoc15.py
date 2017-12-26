def next_value(initial, factor, divider):
    while True:
        next = initial * factor % divider 
        yield next
        initial = next

def match_count(gen_a, gen_b, count):
    num_match = 0
    mask = int('1' * 16, 2)
    for i in range(count):
        a = next(gen_a) & mask
        b = next(gen_b) & mask
        if a == b:
            num_match += 1
    return num_match

if __name__ == '__main__':
    factor_a = 16807
    factor_b = 48271
    starting_a_test = 65
    starting_b_test = 8921
    starting_a = 703
    starting_b = 516
    divider = 2147483647

    gen_a = next_value(starting_a, factor_a, divider)
    gen_b = next_value(starting_b, factor_b, divider)

    print(match_count(gen_a, gen_b, 40000000))
