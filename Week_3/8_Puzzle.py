import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def manhattan(state):

    distance = 0
    for i in range(9):
        if state[i] == 0:
            continue
        goal_index = GOAL.index(state[i])
        x1, y1 = divmod(i, 3)
        x2, y2 = divmod(goal_index, 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


def get_neighbors(state):

    neighbors = []
    zero_index = state.index(0)
    x, y = divmod(zero_index, 3)

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_index = nx * 3 + ny
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = \
                new_state[new_index], new_state[zero_index]
            neighbors.append(tuple(new_state))

    return neighbors


def a_star(start):

    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, [start]))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == GOAL:
            return path

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (g + 1 + manhattan(neighbor),
                     g + 1,
                     neighbor,
                     path + [neighbor])
                )

    return None



start_state = (1, 2, 3,
               4, 0, 6,
               7, 5, 8)

solution = a_star(start_state)

if solution:
    print("Solution steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
