from collections import deque

def bfs(capacities, target):
    A_cap, B_cap, C_cap = capacities
    start = (A_cap, 0, 0)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        (a, b, c), path = queue.popleft()

        # Goal check
        if a == target or b == target or c == target:
            return path

        next_states = []

        # Fill
        next_states.append((A_cap, b, c))
        next_states.append((a, B_cap, c))
        next_states.append((a, b, C_cap))

        # Empty
        next_states.append((0, b, c))
        next_states.append((a, 0, c))
        next_states.append((a, b, 0))

        # Pour operations
        def pour(x, y, cap_y):
            transfer = min(x, cap_y - y)
            return x - transfer, y + transfer

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

        # Explore neighbors
        for ns in next_states:
            if ns not in visited:
                visited.add(ns)
                queue.append((ns, path + [ns]))

    return None


# Example run
solution = bfs((8,5,3), 4)
print("Shortest path:")
for step in solution:
    print(step)