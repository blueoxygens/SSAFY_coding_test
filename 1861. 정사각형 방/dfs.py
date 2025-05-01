import sys

sys.stdin = open("input.txt", "r")

def routing(x, y, N, rooms, dp):
    if dp[y][x]:  # 이미 계산된 경우
        return dp[y][x]
    
    max_hop = 1  # 자기 자신 포함
    for dx, dy in ((1,0), (-1,0), (0,-1), (0,1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and rooms[ny][nx] == rooms[y][x] + 1:
            max_hop = max(max_hop, 1+ routing(nx, ny, N, rooms, dp))
        elif 0 <= nx < N and 0 <= ny < N and rooms[ny][nx] != rooms[y][x] + 1:
            continue
    
    dp[y][x] = max_hop
    return max_hop

#------------------------------------------------------------------------------------------------------
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0]*N for _ in range(N)]

    max_move = 0
    max_start = N+1

    for y in range(N):
        for x in range(N):
            if rooms[y][x] == N:
                continue
            hop = routing(x, y, N, rooms, dp)
            if hop > max_move or (hop == max_move and rooms[y][x] < max_start):
                max_move = hop
                max_start = rooms[y][x]

    print(f'#{tc} {max_start} {max_move}')
