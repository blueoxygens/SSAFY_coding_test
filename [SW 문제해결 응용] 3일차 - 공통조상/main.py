import sys
from collections import defaultdict, deque

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    V, E, n1, n2 = map(int, input().split())
    
    edges = defaultdict(list)
    parent = defaultdict(int) 
    
    inputs = list(map(int, input().split()))
    
    for i in range(0, 2 * E - 1, 2):
        p, c = inputs[i], inputs[i+1]
        edges[p].append(c)
        parent[c] = p

    ancestors_n1 = set()
    temp = n1
    while temp != 0:
        ancestors_n1.add(temp)
        temp = parent[temp]

    lca = n2 
    while lca not in ancestors_n1:
        lca = parent[lca]

    count = 0
    q = deque([lca])
    
    while q:
        target = q.popleft()
        count += 1
        if target in edges:
            q.extend(edges[target])
            
    print(f'#{tc} {lca} {count}')