from collections import deque
def min_time(grid):
    n = len(grid)
    if n == 0 or len(grid[0]) == 0:
        return -1
    queue = deque([(0, 0, 0)]) 
    visited = set()
    min_time = [[float('inf')] * n for _ in range(n)]
    min_time[0][0] = grid[0][0]

    while queue:
        time, x, y = queue.popleft()
        if (x, y) == (n - 1, n - 1):
            return time
        visited.add((x, y))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited:
                new_time = time + grid[new_x][new_y]
                if new_time < min_time[new_x][new_y]:
                    min_time[new_x][new_y] = new_time
                    queue.append((new_time, new_x, new_y))
    return -1 
grid = [
    [1, 2, 0],
    [2, 0, 1],
    [1, 2, 1]
]
result = min_time(grid)
print("Minimum time to reach:", result)
