from collections import deque
def water_jug():
    a, b = 4, 3
    target = 2
    queue = deque([(0, 0)])
    visited = set()
    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print(x, y)
        if x == target or y == target:
            print("Goal reached!")
            return
        next_states = [
            (a, y),                  # Fill Jug A
            (x, b),                  # Fill Jug B
            (0, y),                  # Empty Jug A
            (x, 0),                  # Empty Jug B
            (x - min(x, b-y), y + min(x, b-y)),  # Pour A to B
            (x + min(y, a-x), y - min(y, a-x))   # Pour B to A
        ]
        for state in next_states:
            if state not in visited:
                queue.append(state)
water_jug()
