import copy

def switch_rows(arr, r0, r1):
    arr[r0], arr[r1] = arr[r1], arr[r0]

def switch_cols(arr, r0, r1):
    for i in range(len(arr[0])):
        arr[i][r0], arr[i][r1] = arr[i][r1], arr[i][r0]

def rotate(arr):
    l = len(arr) - 1
    tmp = [None] * l

    for i in range(l):
        arr[l - i][0], tmp[l - i - 1] = arr[0][i], arr[l - i][0]
    for i in range(l):
        arr[-1][l - i], tmp[l - i - 1] = tmp[l - i - 1], arr[-1][l - i]
    for i in range(l):
        arr[i][-1], tmp[l - i - 1] = tmp[l - i - 1], arr[i][-1]
    for i in range(l):
        arr[0][i] = tmp[l - i  - 1]

class Rule():
    def __init__(self, input_format):
        self.input_format = input_format
        arr = [list(l) for l in input_format.split('/')]
        self.permutations = Rule.create_permutations(arr)

    def print_permutations(self):
        for p in self.permutations:
            print('{0}\n'.format(p))
    
    @staticmethod
    def create_permutations(arr):
        permutations = set()

        permutations.add(RulePermutation(arr))

        #flip vertical
        arrcpy = copy.deepcopy(arr)
        switch_rows(arrcpy, 0, -1)
        permutations.add(RulePermutation(arrcpy))

        #flip horizontal
        arrcpy = copy.deepcopy(arr)
        switch_cols(arrcpy, 0, -1)
        permutations.add(RulePermutation(arrcpy))

        arrcpy = arr
        for i in range(3):
            arrcpy = copy.deepcopy(arrcpy)
            rotate(arrcpy)
            rp = RulePermutation(arrcpy)
            if rp in permutations:
                print('Already in permutations!')
            
            permutations.add(rp)

        return permutations

    
class RulePermutation():
    def __init__(self, arr):
        self.arr = arr

    def __str__(self):
        joined_cols = [''.join(row) for row in self.arr]
        return '\n'.join(joined_cols)

    def __hash__(self):
        return hash(self.input_format())

    def input_format(self):
        joined_cols = [''.join(row) for row in self.arr]
        return '/'.join(joined_cols)

if __name__ == '__main__':
    #test = '.#./..#/###'
    test = '123/894/765'
    # arr = [list(l) for l in test.split('/')]

    # joined_cols = [''.join(row) for row in arr]
    # print('\n'.join(joined_cols))

    # print('\n')
    # rotate(arr)

    # joined_cols = [''.join(row) for row in arr]
    # print('\n'.join(joined_cols))

    rule = Rule(test)
    rule.print_permutations()