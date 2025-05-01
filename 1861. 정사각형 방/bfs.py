from collections import deque
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    max_hop = 0
    min_start = float('inf')

    for y in range(N):
        for x in range(N):
            q = deque()
            q.append((x, y, 1))  # (x, y, 현재까지 이동 거리)
            start_num = rooms[y][x]

            while q:
                cx, cy, cnt = q.popleft()

                for dx, dy in ((1,0), (-1,0), (0,-1), (0,1)):
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < N and 0 <= ny < N and rooms[ny][nx] == rooms[cy][cx] + 1:
                        q.append((nx, ny, cnt + 1))
                        break  # 한 방향으로만 갈 수 있으므로 break

            if cnt > max_hop:
                max_hop = cnt
                min_start = start_num
            elif cnt == max_hop and start_num < min_start:
                min_start = start_num

    print(f"#{tc} {min_start} {max_hop}")
