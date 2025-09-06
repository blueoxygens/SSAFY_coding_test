import sys
import math
from collections import defaultdict

sys.stdin = open("1_sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    node = list(map(int, input().split(" ")))
    #Backtracking?
    nodemap = defaultdict(list)

    for i in range(N-1):
        if i == N-2:
            nodemap[i].append((i+1, abs(node[i+1] - node[i])))
        else:
            nodemap[i].append((i+1, abs(node[i+1] - node[i])))
            nodemap[i].append((i+2, abs(node[i+2] - node[i])))
    
    print(nodemap)

    ans = math.inf
    
    for i in range(1, N-1):
        temp = 0
        for j in range(N-1):
            if j == i:
                continue
            if j == i-1:
                temp += nodemap[j][1][1]
            else:
                temp += nodemap[j][0][1]
        if temp < ans:
            ans = temp
    
    print(ans)