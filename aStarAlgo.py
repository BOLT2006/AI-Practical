import heapq                                   # heapq gives us a priority queue (smallest item pops first)

# STEP 1: DATA
start = (1, 2, 3,                              # start board, row 1
         4, 0, 6,                              # row 2 (0 is the blank space)
         7, 5, 8)                              # row 3

goal = (1, 2, 3,                               # goal board, row 1
        4, 5, 6,                               # row 2
        7, 8, 0)                               # row 3 (blank is at the last position)


# STEP 2: HEURISTIC (count misplaced tiles)
def h(state):                                  # takes a board, returns a guess of moves left
    count = 0                                  # start counting wrong tiles from zero

    for i in range(9):                         # check all 9 positions (0 to 8)
        if state[i] != 0 and state[i] != goal[i]:   # tile is not blank AND not in its goal position
            count += 1                         # so it is misplaced, add 1

    return count                               # return the number of misplaced tiles


# A* Algorithm
def astar():                                   # main function that runs A*

    # STEP 3: SETUP
    pq = []                                    # empty priority queue (a list used as a heap)
    heapq.heappush(pq, (h(start), 0, start))   # push start as (f, g, state); f = h(start) since g = 0

    visited = set()                            # set of boards already explored

    while pq:                                  # keep going while there are boards left to try

        # STEP 4: POP, VISITED, GOAL
        f, g, state = heapq.heappop(pq)        # take the board with the smallest f

        if state in visited:                   # did we already explore this board?
            continue                           # yes, skip it and take the next one

        visited.add(state)                     # mark this board as explored

        print("State:", state)                 # print the board being explored

        if state == goal:                      # is this the goal board?
            print("Goal Reached!")             # yes, announce it
            print("Total Moves:", g)           # g = number of moves made to get here
            return                             # stop the algorithm

        # STEP 5: FIND BLANK, LIST MOVES
        pos = state.index(0)                   # position (0 to 8) of the blank

        moves = [-3, 3, -1, 1]                 # blank moves: up, down, left, right

        for move in moves:                     # try each of the 4 moves

            new_pos = pos + move               # where the blank would end up

            # STEP 6: BOUNDARY CHECKS
            if new_pos < 0 or new_pos > 8:     # off the top or bottom of the board
                continue                       # invalid move, skip it

            if move == -1 and pos % 3 == 0:    # moving left from the left column would wrap to previous row
                continue                       # invalid move, skip it

            if move == 1 and pos % 3 == 2:     # moving right from the right column would wrap to next row
                continue                       # invalid move, skip it

            # STEP 7: SWAP
            new_state = list(state)            # tuple can't be changed, so copy it as a list

            new_state[pos], new_state[new_pos] = new_state[new_pos], new_state[pos]   # swap blank with the neighbour tile

            new_state = tuple(new_state)       # convert back to tuple so it can go in a set/heap

            # STEP 8: PUSH
            if new_state not in visited:       # only consider boards we haven't explored

                new_g = g + 1                  # one more move than the parent board

                new_f = new_g + h(new_state)   # f = moves so far + estimated moves left

                heapq.heappush(pq, (new_f, new_g, new_state))   # add to the queue; smallest f will pop first


astar()                                        # run the program