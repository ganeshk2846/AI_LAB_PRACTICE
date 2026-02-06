import heapq

CAP_A = 4   
CAP_B = 3   
GOAL = 2


class State:
    def __init__(self, a, b, g=0, parent=None):
        self.a = a          
        self.b = b          
        self.g = g         
        self.parent = parent

    def h(self):
        """Heuristic function"""
        return min(abs(self.a - GOAL), abs(self.b - GOAL))

    def f(self):
        """Evaluation function"""
        return self.g + self.h()

    def is_goal(self):
        return self.a == GOAL or self.b == GOAL

    def get_successors(self):
        successors = []

        successors.append(State(CAP_A, self.b, self.g + 1, self))
        successors.append(State(self.a, CAP_B, self.g + 1, self))

        successors.append(State(0, self.b, self.g + 1, self))
        successors.append(State(self.a, 0, self.g + 1, self))

        transfer = min(self.a, CAP_B - self.b)
        successors.append(
            State(self.a - transfer, self.b + transfer, self.g + 1, self)
        )

        transfer = min(self.b, CAP_A - self.a)
        successors.append(
            State(self.a + transfer, self.b - transfer, self.g + 1, self)
        )

        return successors

    def __lt__(self, other):
        """Needed for priority queue"""
        return self.f() < other.f()

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __hash__(self):
        return hash((self.a, self.b))


def reconstruct_path(state):
    path = []
    while state:
        path.append((state.a, state.b))
        state = state.parent
    return path[::-1]


def a_star():
    start = State(0, 0)
    open_list = []
    closed_set = set()

    heapq.heappush(open_list, start)

    while open_list:
        current = heapq.heappop(open_list)

        if current.is_goal():
            return reconstruct_path(current)

        closed_set.add(current)

        for successor in current.get_successors():
            if successor in closed_set:
                continue
            heapq.heappush(open_list, successor)

    return None



solution = a_star()

if solution:
    print("Solution path:")
    for step in solution:
        print(step)
else:
    print("No solution found")
   