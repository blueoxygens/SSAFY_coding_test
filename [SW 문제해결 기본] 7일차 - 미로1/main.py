import sys
sys.stdin = open("input.txt", "r")

def dfs(maze, x, y, directions, visited):
    if maze[x][y] == 3:
        return 1
    visited.add((x, y))
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 16 and 0 <= ny < 16 and (nx, ny) not in visited and maze[nx][ny] != 1:
            if dfs(maze, nx, ny, directions, visited):
                return 1
    return 0

directions = [(1,0), (-1,0), (0,1), (0,-1)]  # 아래, 위, 오른쪽, 왼쪽

for _ in range(10):
    tc = int(input())
    maze = [list(map(int, list(input().strip()))) for _ in range(16)]
    visited = set()
    if dfs(maze, 1, 1, directions, visited):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
