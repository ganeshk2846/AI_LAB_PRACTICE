# Cybersecurity Attack-Defense Simulation using Minimax + Alpha-Beta Pruning

# Attack-Defense Game Tree Example
# Max Player: Defender (tries to maximize system security)
# Min Player: Attacker (tries to minimize system security)

# Leaf node values (system security scores after sequences of actions)
# Positive = secure, Negative = compromised
values = [10, -10, 5, -5, 7, -7, 3, -3]

import math

# Alpha-Beta Pruning Algorithm
def alpha_beta(depth, node_index, is_max, alpha, beta, values, height):
    # If leaf node, return its value
    if depth == height:
        return values[node_index]

    if is_max:
        best = -math.inf
        for i in range(2):  # Two possible moves: e.g., defend actions
            val = alpha_beta(depth + 1, node_index*2 + i, False, alpha, beta, values, height)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # Beta cutoff
        return best
    else:
        best = math.inf
        for i in range(2):  # Two possible moves: e.g., attack actions
            val = alpha_beta(depth + 1, node_index*2 + i, True, alpha, beta, values, height)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break  # Alpha cutoff
        return best

# Tree height (3 levels)
height = 3  # Max → Min → Max

# Run Alpha-Beta
optimal_value = alpha_beta(0, 0, True, -math.inf, math.inf, values, height)
print("Optimal System Security Value (Defender):", optimal_value)