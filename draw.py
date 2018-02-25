'''
Two kinds of mazes:
- perfect: every cell can reach every other cell by exactly one path. Thus no
  loops, intersections, etc.
- braid: can have multiple paths, loops, etc
'''

def draw_cells(width: int, height: int):
    for column in range(width):
        print("■---", end='')
    print("■")
    for row in range(height):
        for column in range(width):
            print("|   ", end='')
        print("|")
        for column in range(width):
            print("■---", end='')
        print("■")


def make_cells(width: int, height: int):
    grid=""
    for column in range(width):
        grid += "■---"
    grid += "■\n"
    for row in range(height):
        for column in range(width):
            grid += "|   "
        grid += "|\n"
        for column in range(width):
            grid += "■---"
        grid += "■"
    return grid
