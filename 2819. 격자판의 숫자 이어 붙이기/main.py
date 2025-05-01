import sys
sys.stdin = open("sample_input.txt", "r")

def dfs(x, y, path):
    if len(path) == 7:
        result.add("".join(path))
        return

    for dx, dy in ((-1,0), (1,0), (0,1), (0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, path + [maze[nx][ny]])

T = int(input())
for tc in range(1, T + 1):
    maze = [input().split() for _ in range(4)] 
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, [maze[i][j]])

    print(f"#{tc} {len(result)}")
