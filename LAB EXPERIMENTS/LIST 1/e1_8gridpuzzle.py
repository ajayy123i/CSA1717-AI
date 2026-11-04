import heapq
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)
def heuristic(state):
    distance = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        goal_index = GOAL.index(tile)
        current_row, current_col = divmod(i, 3)
        goal_row, goal_col = divmod(goal_index, 3)
        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)
    return distance
def is_solvable(state):
    tiles = [x for x in state if x != 0]
    inversions = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1
    return inversions % 2 == 0
def get_neighbors(state):
    zero = state.index(0)
    row, col = divmod(zero, 3)
    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]
    neighbors = []
    for dr, dc in moves:
        nr = row + dr
        nc = col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_zero = nr * 3 + nc
            new_state = list(state)
            new_state[zero], new_state[new_zero] = (
                new_state[new_zero], new_state[zero]
            )
            neighbors.append(tuple(new_state))
    return neighbors
def solve(start):
    if not is_solvable(start):
        print("The puzzle is not solvable.")
        return
    pq = [(heuristic(start), 0, start)]
    cost = {start: 0}
    parent = {start: None}
    while pq:
        f, g, current = heapq.heappop(pq)
        if g != cost.get(current):
            continue
        if current == GOAL:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            print("Solution found!")
            print("Number of moves:", len(path) - 1)
            for step, state in enumerate(path):
                print(f"\nStep {step}:")
                for i in range(0, 9, 3):
                    print(*state[i:i + 3])
            return
        for neighbor in get_neighbors(current):
            new_cost = g + 1
            if new_cost < cost.get(neighbor, float("inf")):
                cost[neighbor] = new_cost
                parent[neighbor] = current
                f_score = new_cost + heuristic(neighbor)
                heapq.heappush(
                    pq, (f_score, new_cost, neighbor)
                )
    print("No solution found.")
print("Enter the 3x3 puzzle (use 0 for the blank):")
values = []
for i in range(3):
    values.extend(map(int, input().split()))

if len(values) != 9 or set(values) != set(range(9)):
    print("Invalid input. Enter each number from 0 to 8 once.")
else:
    solve(tuple(values))
