import sys
from collections import deque

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # BFS
    N = int(input())
    pan = []
    for i in range(N):
        line = list(map(int, list(input())))
        pan.append(line)
    result = [[float('inf') for i in range(N)] for j in range(N)]
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    def bfs(a, b):
        q = deque()
        q.append((a,b))
        result[a][b]=0
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx<0 or ny<0 or nx>=N or ny>=N:
                    continue
                if result[x][y]+pan[nx][ny] < result[nx][ny]: 
                    result[nx][ny] = result[x][y]+pan[nx][ny]
                    q.append((nx,ny))
    bfs(0,0)
    print(f'#{test_case} {result[N-1][N-1]}')