# -----------
# User Instructions:
#
# Modify the the search function so that it becomes
# an A* search algorithm as defined in the previous
# lectures.
#
# Your function should return the expanded grid
# which shows, for each element, the count when
# it was expanded or -1 if the element was never expanded.
#
# If there is no path from init to goal,
# the function should return the string 'fail'
# ----------

grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 0],
        [1, 1, 0, 0, 1, 0]]
# heuristic = [[9, 8, 7, 6, 5, 4],
#              [8, 7, 6, 5, 4, 3],
#              [7, 6, 5, 4, 3, 2],
#              [6, 5, 4, 3, 2, 1],
#              [5, 4, 3, 2, 1, 0]]
cost = [[1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1]]

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def make_heuristic(grid, goal, cost):
    heuristic = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            heuristic[i][j] = abs(i - goal[0]) + abs(j - goal[1])
    return heuristic

def search(grid, init, goal, cost, heuristic):
    # ----------------------------------------
    # modify the code below
    # ----------------------------------------
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed[init[0]][init[1]] = 1

    expand = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]
    action = [[-1 for col in range(len(grid[0]))] for row in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = g + h
    open = [[f, g, h, x, y]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand
    count = 0

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            f = next[0]
            g = next[1]
            h = next[2]
            x = next[3]
            y = next[4]
            expand[x][y] = count
            count += 1

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                # max = len(heuristic) * len(heuristic[0])
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            h2 = heuristic[x2][y2]
                            f2 = g2 + h2
                            # max2 = heuristic[x2][y2] + g2
                            # if max2 < max:
                            #     max = max2
                            #     next = [f2, g2, h2, x2, y2]
                            open.append([f2, g2, h2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i
                # open.append(next)
    invpath = []
    x = goal[0]
    y = goal[1]
    invpath.append([x, y])
    while x != init[0] or y != init[1]:
        x2 = x - delta[action[x][y]][0]
        y2 = y - delta[action[x][y]][1]
        x = x2
        y = y2
        invpath.append([x, y])

    path = []
    for i in range(len(invpath)):
        path.append(invpath[len(invpath) - 1 - i])
    return expand,path

heuristic = make_heuristic(grid, goal, cost)
expand,path = search(grid, init, goal, cost, heuristic)

for i in range(len(expand)):
    print expand[i]
for i in range(len(path)):
    print path[i]