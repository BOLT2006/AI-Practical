
# DFS for Water Jug Problem

capacity1 = 4
capacity2 = 3
goal = 2

stack = [(0, 0)]
visited = set()
parent = {(0, 0): None}

while stack:

    state = stack.pop()

    if state in visited:
        continue

    visited.add(state)

    x, y = state

    # Check goal
    if x == goal or y == goal:
        print("Solution Found!")
        break

    # Generate possible operations
    next_states = [
        (capacity1, y),  # Fill jug 1
        (x, capacity2),  # Fill jug 2
        (0, y),          # Empty jug 1
        (x, 0),           # Empty jug 2
        (x - min(x, capacity2-y), y + min(x, capacity2-y)), # Pour 1 to 2
        (x + min(y, capacity1-x), y - min(y, capacity1-x))  # Pour 2 to 1
    ]

    for new_state in next_states:

        if new_state not in visited and new_state not in parent:
            parent[new_state] = state
            stack.append(new_state)

# Print solution path
if x == goal or y == goal:

    path = []

    while state is not None:
        path.append(state)
        state = parent[state]

    path.reverse()

    print("Solution Path:")

    for step in path:
        print(step)

else:
    print("No solution found")
