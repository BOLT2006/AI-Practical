
import random

# Distance matrix
dist = [
    [0, 10, 15, 20, 18, 12],
    [10, 0, 35, 25, 17, 28],
    [15, 35, 0, 30, 28, 20],
    [20, 25, 30, 0, 22, 16],
    [18, 17, 28, 22, 0, 14],
    [12, 28, 20, 16, 14, 0]
]

cities = [0, 1, 2, 3, 4, 5]

# Calculate total tour distance
def cost(tour):
    total = 0

    for i in range(len(tour)):
        total += dist[tour[i]][tour[(i + 1) % len(tour)]]

    return total


# Local Beam Search
k = 4
beam = []

# Generate initial tours
for i in range(k):
    tour = cities[:]
    random.shuffle(tour)
    beam.append(tour)

best_tour = min(beam, key=cost)
best_cost = cost(best_tour)

# Search iterations
for iteration in range(10):

    neighbours = []

    for tour in beam:
        for i in range(1, len(tour)):
            for j in range(i + 1, len(tour)):

                new_tour = tour[:]
                new_tour[i], new_tour[j] = new_tour[j], new_tour[i]

                if new_tour not in neighbours:
                    neighbours.append(new_tour)

    # Select best k neighbours
    neighbours.sort(key=cost)
    beam = neighbours[:k]

    # Update global best
    if cost(beam[0]) < best_cost:
        best_tour = beam[0][:]
        best_cost = cost(best_tour)

    print("Iteration:", iteration + 1,
          "Best Cost:", cost(beam[0]),
          "Global Best:", best_cost)

# Final result
names = ['A', 'B', 'C', 'D', 'E', 'F']

print("\nBest Tour:")
print(" -> ".join(names[i] for i in best_tour), "->", names[best_tour[0]])

print("Total Distance:", best_cost)
