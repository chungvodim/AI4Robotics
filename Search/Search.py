# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1
delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

# def search(grid,init,goal,cost):
#     if init == goal:
#         print "result: ", [cost, init[0], init[1]]
#     else:
#         print "take the list", [cost, init[0], init[1]]
#         x = init[0]
#         y = init[1]
#         if x - 1 >= 0 and grid[x - 1][y] == 0:
#             print "new open list:", [cost + 1, x - 1, y]
#             search(grid, [x - 1, y], goal, cost + 1)
#         if y - 1 >= 0 and grid[x][y - 1] == 0:
#             print "new open list:", [cost + 1, x, y - 1]
#             search(grid, [x, y - 1], goal, cost + 1)
#         if x + 1 <= goal[0] and y <= goal[1] and grid[x + 1][y] == 0:
#             print "new open list:", [cost + 1, x + 1, y]
#             search(grid,[x + 1, y], goal, cost + 1)
#         if x <= goal[0] and y + 1 <= goal[1] and grid[x][y + 1] == 0:
#             print "new open list:", [cost + 1, x, y + 1]
#             search(grid, [x, y + 1], goal, cost + 1)

def search(grid,init,goal,cost):
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    action = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False # flag set when search complete
    resign = False # flag set if we can't find expand
    count = 0
    while not found and not resign:
        # check if we still have elements on the open list
        if len(open) == 0:
            resign = True
            print 'Fail' # search terminated without success
        else:
            # remove node from the list
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            expand[x][y] = count
            count += 1
            # check if we are done
            if x == goal[0] and y == goal[1]:
                found = True
                # expand[x][y] = '*'
                # print next
            else:
                # expand winning element and add to new open list
                for i in range(len(delta)):
                    x2 =  x + delta[i][0]
                    y2 =  y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2,x2,y2])
                            closed[x2][y2] = 1
                            action[x][y] = i
    return expand,action


expand,action = search(grid,init,goal,cost)
for i in range(len(expand)):
        print expand[i]
print '-------------------'
for i in range(len(action)):
    print action[i]

policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
x = goal[0]
y = goal[1]
policy[x][y] = '*'
# while x != init[0]and y != init[1]:
#     x2 = x - delta[action[x][y]][0]
#     y2 = y - delta[action[x][y]][1]
#     policy[x2][y2] = delta_name[action[x][y]]
#     x = x2
#     y = y2
# for i in range(len(policy)):
#     print policy[i]