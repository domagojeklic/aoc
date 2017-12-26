from aoc10 import knot_hash

def num_squares(input):
    num = 0
    grid = []
    for i in range(128):
        hash = knot_hash('{0}-{1}'.format(input, i))
        bin_row = bin(int(hash, 16))[2:].zfill(128)
        num += bin_row.count('1')
        grid.append(list(bin_row))
    return num, grid

def adjacent_squares(row, col, grid_len):
    squares = []
    if is_valid(row - 1, col, grid_len):
        squares.append((row - 1, col))
    if is_valid(row + 1, col, grid_len):
        squares.append((row + 1, col))
    if is_valid(row, col - 1, grid_len):
        squares.append((row, col - 1))
    if is_valid(row, col + 1, grid_len):
        squares.append((row, col + 1))
    
    return squares

def is_valid(row, col, grid_len):
    return row >= 0 and col >= 0 and row < grid_len and col < grid_len

def expand_region(grid, row, col):
    grid[row][col] = '0'
    adjacent = adjacent_squares(row, col, len(grid))
    for x, y in adjacent:
        if grid[x][y] == '1':
            expand_region(grid, x, y)


def num_regions(grid):
    num = 0
    grid_len = len(grid)
    for row in range(grid_len):
        for col in range(grid_len):
            if grid[row][col] == '1':
                num += 1
                expand_region(grid, row, col)
    return num

if __name__ == '__main__':
    # input = 'flqrgnkx'
    input = 'nbysizxe' 
    (num, grid) = num_squares(input)
    print('Result part 1: {0}'.format(num))
    print('Result part 2: {0}'.format(num_regions(grid)))