
def coords_key(x, y):
    return '{0},{1}'.format(x, y)

def coord_value(spiral, x, y):
    total = 0
    for ix in range(x - 1, x + 2):
        for iy in range(y - 1, y + 2):
            if x == ix and y == iy:
                continue
            total += spiral.get(coords_key(ix, iy), 0)
    return total

def process_direction(spiral, x, y, dx, dy, r, limit):
    for i in r:
        x += dx
        y += dy
        val = coord_value(spiral, x, y)
        spiral[coords_key(x, y)] = val
        if val > limit:
            return (val, x, y)
    
    return (-1, x, y)

def create_spiral(n):
    x = 0
    y = 0
    spiral_num = 0
    spiral = {}
    spiral[coords_key(x,y)] = 1
    while True:
        spiral_num += 1
        spiral_dimension = 1 + spiral_num * 2

        x += 1
        spiral[coords_key(x, y)] = coord_value(spiral, x, y)

        (val, x, y) = process_direction(spiral, x, y, 0, 1, range(0, spiral_dimension -2), n)
        if val > 0 : return val

        (val, x, y) = process_direction(spiral, x, y, -1, 0, range(0, spiral_dimension -1), n)
        if val > 0 : return val

        (val, x, y) = process_direction(spiral, x, y, 0, -1, range(0, spiral_dimension -1), n)
        if val > 0 : return val

        (val, x, y) = process_direction(spiral, x, y, 1, 0, range(0, spiral_dimension -1), n)
        if val > 0 : return val
          
    return spiral
            

if __name__ == '__main__':
    input = 265149
    print(create_spiral(input))