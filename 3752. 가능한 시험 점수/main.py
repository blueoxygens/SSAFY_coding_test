import sys
from collections import deque

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    case_n = int(input())
    arr = list(map(int, input().strip().split()))
    
    if case_n == 0:
        print(f'#{tc} 1')
        continue
    
    score_tree = [[] for _ in range(case_n+1)]
    score_tree[0] = [0]

    for i in range(1, case_n+1):
        for j in range(0, 2**i, 2):
            parent = score_tree[i-1][j//2]
            score_tree[i].append(parent)  # No score added
            score_tree[i].append(parent + arr[i-1])  # Score added
    
    unique_scores = len(set(score_tree[case_n]))
    
    print(f'#{tc} {unique_scores}')