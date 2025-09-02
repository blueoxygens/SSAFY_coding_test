import sys
sys.stdin = open("re_sample_input.txt", "r")

class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0]*n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: 
            return False
        if self.r[a] < self.r[b]:
            a, b = b, a
        self.p[b] = a
        if self.r[a] == self.r[b]:
            self.r[a] += 1
        return True

T = int(sys.stdin.readline())
for tc in range(1, T+1):
    N = int(sys.stdin.readline().strip())
    X = list(map(int, sys.stdin.readline().split()))
    Y = list(map(int, sys.stdin.readline().split()))
    E = float(sys.stdin.readline().strip())

    # 1) 간선: (제곱거리, u, v), 중복/자기루프 제거 (j>i)
    edges = []
    for i in range(N):
        xi, yi = X[i], Y[i]
        for j in range(i+1, N):
            dx = xi - X[j]
            dy = yi - Y[j]
            w2 = dx*dx + dy*dy  # 제곱거리 그대로
            edges.append((w2, i, j))

    # 2) 가중치 오름차순 정렬
    edges.sort(key=lambda e: e[0])

    # 3) Kruskal with DSU
    dsu = DSU(N)
    picked = 0
    total_w2 = 0  # 제곱거리의 합
    for w2, u, v in edges:
        if dsu.union(u, v):
            total_w2 += w2
            picked += 1
            if picked == N - 1:
                break

    # 4) 비용 계산: E * sum(w2) (문제에 따라 round)
    # SWEA 1251 '하나로' 기준: 반올림
    cost = round(E * total_w2)
    print(f"#{tc} {cost}")
