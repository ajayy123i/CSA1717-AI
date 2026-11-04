graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'E': 1},
    'D': {'G': 5},
    'E': {'G': 3},
    'G': {}
}
h = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 4,
    'E': 2,
    'G': 0
}
def astar(start, goal):
    open_list = [(h[start], 0, start, [start])]
    best = {start: 0}
    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)
        if g != best.get(node):
            continue
        if node == goal:
            print("Path:", path)
            print("Cost:", g)
            return
        for neighbor, cost in graph[node].items():
            new_g = g + cost

            if new_g < best.get(neighbor, float('inf')):
                best[neighbor] = new_g
                new_f = new_g + h[neighbor]
                open_list.append(
                    (new_f, new_g, neighbor, path + [neighbor])
                )
    print("No path found")
astar('A', 'G')
