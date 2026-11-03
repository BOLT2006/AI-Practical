# def toh(n, source, auxiliary, destination):

#     # Base case
#     if n == 1:
#         print(f"Move disk 1 from {source} to {destination}")
#         return

#     # Move n-1 disks from source to auxiliary
#     toh(n-1, source, destination, auxiliary)

#     # Move largest disk to destination
#     print(f"Move disk {n} from {source} to {destination}")

#     # Move n-1 disks from auxiliary to destination
#     toh(n-1, auxiliary, source, destination)


# toh(3, 'A', 'B', 'C')


































# State Space Search using BFS for Tower of Hanoi

from collections import deque  # Import deque to implement Queue

n = int(input("Enter number of disks: "))  # Take number of disks from user

# Create initial state and goal state
start = (tuple(range(n, 0, -1)), (), ())  # All disks are initially on rod A
goal = ((), (), tuple(range(n, 0, -1)))   # All disks should be on rod C

queue = deque([start])  # Insert initial state into the queue
visited = {start}       # Store visited states to avoid repetition
parent = {start: None}  # Store previous state of each state
move = {}               # Store disk movement information

# BFS search starts
while queue:  # Continue until the queue becomes empty

    state = queue.popleft()  # Remove the first state from the queue

    if state == goal:  # Check whether the goal state is reached
        break          # Stop searching if goal is found

    # Check all possible source and destination rods
    for i in range(3):  # Select source rod (A, B, C)
        for j in range(3):  # Select destination rod (A, B, C)

            # Skip if source and destination are same or source is empty
            if i == j or not state[i]:
                continue

            pegs = [list(p) for p in state]  # Convert tuples into lists
            disk = pegs[i][-1]  # Get the top disk from source rod

            # Check whether destination is empty or top disk is bigger
            if not pegs[j] or disk < pegs[j][-1]:

                pegs[i].pop()       # Remove disk from source rod
                pegs[j].append(disk)  # Add disk to destination rod

                # Convert lists back into tuples to create new state
                new_state = tuple(tuple(p) for p in pegs)

                # Check whether this state is already visited
                if new_state not in visited:

                    visited.add(new_state)  # Mark new state as visited
                    parent[new_state] = state  # Store previous state
                    move[new_state] = (disk, i, j)  # Store disk movement
                    queue.append(new_state)  # Add new state to queue

# Print the solution
path = []  # Create empty list to store solution moves
current = goal  # Start tracing backwards from goal state

# Trace the path from goal state to initial state
while current != start:

    path.append(move[current])  # Store the movement
    current = parent[current]   # Move to previous state

path.reverse()  # Reverse path to get correct movement order

names = ['A', 'B', 'C']  # Assign names to rods (0=A, 1=B, 2=C)

print("\nInitial State:", start)  # Display initial state

# Print each disk movement
for disk, i, j in path:
    print("Move disk", disk, "from", names[i], "to", names[j])

print("\nGoal State:", goal)  # Display final state
print("Total Moves:", len(path))  # Display total number of moves
