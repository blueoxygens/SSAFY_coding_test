import sys
from collections import deque

def countSafe(wm, x, y, N):
    if wm[y][x] == '*':
        return -1
    count = 0
    for dx, dy in ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and wm[ny][nx] == '*':
            count += 1
    return count

def bfs(start_x, start_y, visited, count_map, world_map, N):
    q = deque()
    q.append((start_x, start_y))
    visited[start_y][start_x] = True

    while q:
        x, y = q.popleft()
        if count_map[y][x] == 0:
            for dx, dy in ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and count_map[ny][nx] != -1:
                    visited[ny][nx] = True
                    if count_map[ny][nx] == 0:
                        q.append((nx, ny))

sys.stdin = open("sample.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    world_map = [list(input().strip()) for _ in range(N)]
    count_map = [[countSafe(world_map, x, y, N) for x in range(N)] for y in range(N)]
    visited = [[False]*N for _ in range(N)]

    count = 0

    # 먼저 0인 지점에서 bfs
    for y in range(N):
        for x in range(N):
            if count_map[y][x] == 0 and not visited[y][x]:
                bfs(x, y, visited, count_map, world_map, N)
                count += 1

    # 그 외 방문 안된 지점은 개별 클릭 필요
    for y in range(N):
        for x in range(N):
            if count_map[y][x] != -1 and not visited[y][x]:
                count += 1

    print(f'#{tc} {count}')
