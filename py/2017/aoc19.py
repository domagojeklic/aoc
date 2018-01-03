from enum import Enum

class Direction(Enum):
    N = 0
    W = 1
    S = 2
    E = 3

def load_maze(filename):
    with open(filename) as f:
        return f.read().split('\n')

def entry_point(maze):
    for i in range(len(maze[0])):
        c = maze[0][i]
        if c == '|':
            return (0, i)

def end_point(x, y, direction, maze):
    point = maze[x][y]
    return point == '+' and len(connecting_points(x, y, direction, maze)) == 0

def valid_point(x, y, maze):
    return x >=0 and y >=0 and x < len(maze) and y < len(maze[0]) and maze[x][y] != ' '

def append_if_valid(x, y, maze, cp):
    if valid_point(x, y, maze):
        cp.append((x, y))

def connecting_points(x, y, direction, maze):
    cp = []
    
    if direction != Direction.N:
        append_if_valid(x + 1, y, maze, cp)
    if direction != Direction.S:
        append_if_valid(x - 1, y, maze, cp)
    if direction != Direction.W:
        append_if_valid(x, y + 1, maze, cp)
    if direction != Direction.E:
        append_if_valid(x, y - 1, maze, cp)
    
    return cp

def point_in_direction(x, y, direction):
    if direction == Direction.N:
        return (x - 1, y)
    elif direction == Direction.S:
        return (x + 1, y)
    elif direction == Direction.E:
        return (x, y + 1)
    elif direction == Direction.W:
        return (x, y - 1)

def move(x, y, direction, maze):
    c = maze[x][y]
    p = point_in_direction(x, y, direction)
    if c == '+':
        cp = connecting_points(x, y, direction, maze)
        if p not in cp:
            p = cp[0]

    d = get_direction(x, y, p[0], p[1])
    
    return (p[0], p[1], d) 

def get_direction(x0, y0, x1, y1):
    if x0 < x1:
        return Direction.S
    elif x0 > x1:
        return Direction.N
    elif y0 < y1:
        return Direction.E
    elif y0 > y1:
        return Direction.W
        

def run_maze(maze):
    solution = []
    direction = Direction.S
    x, y = entry_point(maze)

    while not end_point(x, y, direction, maze):
        c = maze[x][y]
        if c.isalpha():
            solution.append(c)
        x, y, direction = move(x, y, direction, maze)

    
    return ''.join(solution)

if __name__ == '__main__':
    maze = load_maze('input19.txt')
    solution = run_maze(maze)
    print(solution)