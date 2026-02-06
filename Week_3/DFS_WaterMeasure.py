# 3 Jug Problem using DFS

# capacities of jugs
A_cap, B_cap, C_cap = 8, 5, 3
target = 4

# DFS function
def dfs(state, visited, path):
    # state is a tuple (a, b, c)
    a, b, c = state

    # goal check
    if a == target or b == target or c == target:
        path.append(state)
        return path

    # mark visited
    visited.add(state)
    path.append(state)

    # generate all possible moves
    next_states = []

    # fill moves
    next_states.append((A_cap, b, c))  # fill A
    next_states.append((a, B_cap, c))  # fill B
    next_states.append((a, b, C_cap))  # fill C

    # empty moves
    next_states.append((0, b, c))      # empty A
    next_states.append((a, 0, c))      # empty B
    next_states.append((a, b, 0))      # empty C

    def pour(x, y, cap_y):
        transfer = min(x, cap_y - y)
        return x - transfer, y + transfer
    # pour moves using function

    # A → B
    na, nb = pour(a, b, B_cap)
    next_states.append((na, nb, c))

    # A → C
    na, nc = pour(a, c, C_cap)
    next_states.append((na, b, nc))

    # B → A
    nb, na = pour(b, a, A_cap)
    next_states.append((na, nb, c))

    # B → C
    nb, nc = pour(b, c, C_cap)
    next_states.append((a, nb, nc))

    # C → A
    nc, na = pour(c, a, A_cap)
    next_states.append((na, b, nc))

    # C → B
    nc, nb = pour(c, b, B_cap)
    next_states.append((a, nb, nc))



    # explore next states
    for ns in next_states:
        if ns not in visited:
            result = dfs(ns, visited, path.copy())
            if result:
                return result

    return None


# initial state: A full, B and C empty
start = (A_cap, 0, 0)
visited = set()
solution_path = dfs(start, visited, [])

# print solution
if solution_path:
    print("Solution path:")
    for step in solution_path:
        print(step)
else:
    print("No solution found.")