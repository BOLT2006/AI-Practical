
import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Count misplaced tiles
def h(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


# A* Algorithm
def astar():

    pq = []
    heapq.heappush(pq, (h(start), 0, start))

    visited = set()

    while pq:

        f, g, state = heapq.heappop(pq)

        if state in visited:
            continue

        visited.add(state)

        print("State:", state)

        if state == goal:
            print("Goal Reached!")
            print("Total Moves:", g)
            return

        pos = state.index(0)

        moves = [-3, 3, -1, 1]

        for move in moves:

            new_pos = pos + move

            if new_pos < 0 or new_pos > 8:
                continue

            if move == -1 and pos % 3 == 0:
                continue

            if move == 1 and pos % 3 == 2:
                continue

            new_state = list(state)

            new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]

            new_state = tuple(new_state)

            if new_state not in visited:

                new_g = g + 1
                new_f = new_g + h(new_state)

                heapq.heappush(pq, (new_f, new_g, new_state))


astar()
