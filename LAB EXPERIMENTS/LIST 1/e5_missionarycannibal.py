from collections import deque
def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    queue = deque([(start, [])])
    visited = set()
    moves = [(1, 0), (2, 0), (0, 1),
             (0, 2), (1, 1)]
    while queue:
        state, path = queue.popleft()
        m, c, boat = state
        if state == goal:
            for step in path + [state]:
                print(step)
            return
        if state in visited:
            continue
        visited.add(state)
        for dm, dc in moves:
            if boat == 1:
                nm, nc, nb = m - dm, c - dc, 0
            else:
                nm, nc, nb = m + dm, c + dc, 1
            if not (0 <= nm <= 3 and 0 <= nc <= 3):
                continue
            left_safe = nm == 0 or nm >= nc
            right_safe = (3 - nm == 0 or
                          3 - nm >= 3 - nc)
            if left_safe and right_safe:
                new_state = (nm, nc, nb)
                if new_state not in visited:
                    queue.append((new_state, path + [state]))
    print("No solution found")

solve()
