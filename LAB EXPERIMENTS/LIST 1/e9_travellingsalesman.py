from itertools import permutations
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
n = len(dist)
cities = range(1, n)
min_cost = float("inf")
best_path = None
for p in permutations(cities):
    path = (0,) + p + (0,)
    cost = 0
    for i in range(n):
        cost += dist[path[i]][path[i + 1]]
    if cost < min_cost:
        min_cost = cost
        best_path = path
print("Best path:", best_path)
print("Minimum cost:", min_cost)
