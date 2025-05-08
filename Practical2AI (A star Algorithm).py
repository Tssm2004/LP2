import heapq

def astar(grid, start, goal):
    h = lambda a, b: abs(a[0]-b[0]) + abs(a[1]-b[1])
    open = [(0, start)]
    came = {}
    g = {start: 0}

    while open:
        _, cur = heapq.heappop(open)
        if cur == goal:
            path = []
            while cur in came:
                path.append(cur)
                cur = came[cur]
            return [start] + path[::-1]

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            n = (cur[0]+dx, cur[1]+dy)
            if 0 <= n[0] < len(grid) and 0 <= n[1] < len(grid[0]) and grid[n[0]][n[1]] == 0:
                ng = g[cur] + 1
                if n not in g or ng < g[n]:
                    g[n] = ng
                    heapq.heappush(open, (ng + h(n, goal), n))
                    came[n] = cur
    return None

# Example
grid = [[0,1,0],[0,0,0],[1,0,0]]
print(astar(grid, (0,0), (2,2)))
