import sys
from collections import defaultdict, deque

sys.stdin = open("input.txt", "r")

# T = int(input())

for _ in range(10):
    tc, num = map(int, input().strip().split(" "))
    edges = list(map(int, input().strip().split(" ")))
    edge_dict = defaultdict(list)
    for i in range(0,len(edges),2):
        edge_dict[edges[i+1]].append(edges[i])
    # print(edge_dict)
    stck = deque()
    stck.append(99)
    cindex = 99
    while stck:
        cindex = stck.pop()
        if cindex == 0:
            print(f'#{tc} 1')
            break
        for child in edge_dict[cindex]:
            stck.append(child)
    if cindex != 0:
        print(f'#{tc} 0')