def subarray(arr, index, length):
    if index + length <= len(arr):
        return arr[index:index+length]
    else:
        return arr[index:] + arr[0:length - (len(arr)-index)]

def replace_subarray(arr, index, subarr):
    for elem in subarr:
        arr[index] = elem
        index = (index + 1) % len(arr)

def process_lengths(elemarr, lenarr, idx = 0, skip_size = 0):
    for l in lenarr:
        moveby = l + skip_size
        subarr = subarray(elemarr, idx, l)
        subarr.reverse()
        replace_subarray(elemarr, idx, subarr)
        idx = (idx + moveby) % len(elemarr)
        skip_size += 1
    
    return (idx, skip_size)

def process_lenarr_ascii(lenarr):
    end_sequence = [17, 31, 73, 47, 23]

    if type(lenarr) == type([]):
        arrstr = str(lenarr)[1:-1]
        arrstr = arrstr.replace(' ', '')
    else:
        arrstr = lenarr
    
    final_arr = [ord(c) for c in arrstr]
    return final_arr + end_sequence

def chunks(l, c):
    for i in range(0, len(l), c):
        yield l[i:i+c]

def xorelements(elemarr):
    result = elemarr[0]
    for i in range(1, len(elemarr)):
        result = result ^ elemarr[i]

    return result

def hex_representation(elem):
    return format(elem, '02x')

def solve_part1(elemlen, lenarr):
    elemarr = list(range(elemlen))
    process_lengths(elemarr, lenarr)
    return elemarr[0] * elemarr[1]

def knot_hash(lenarr, elemlen = 256):
    result = ''
    numrounds = 64
    chunk_size = 16
    elemarr = list(range(elemlen))
    lenarr = process_lenarr_ascii(lenarr)
    idx = 0
    skip_size = 0

    for _ in range(numrounds):
        (idx, skip_size) = process_lengths(elemarr, lenarr, idx, skip_size)
    for subarr in chunks(elemarr, chunk_size):
        result += hex_representation(xorelements(subarr))
    
    return result

if __name__ == '__main__':
    elemlen = 256
    lenarr = [183, 0, 31, 146, 254, 240, 223, 150, 2, 206, 161, 1, 255, 232, 199, 88]
    
    print('Result part 1 = {0}'.format(solve_part1(elemlen, lenarr)))
    print('Result part 2 = {0}'.format(knot_hash(lenarr)))