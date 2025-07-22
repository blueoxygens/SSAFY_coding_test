import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().strip().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    tree = []
    min_gap =99999
    for i in range(1, N+1):
        tree.append([0]*2**i)
    #차 변수 abs(node-B)
    tree[0][0], tree[0][1] = 0, arr[0]
    if tree[0][1] >= B:
        min_gap = abs(B-tree[0][1])
    for i in range(1, N):
        endf = False
        for j in range(0,2**(i+1),2):
            tree[i][j], tree[i][j+1] = tree[i-1][j//2], tree[i-1][j//2]+arr[i]
            left = tree[i][j]
            right = tree[i][j+1]
            if left >= B and right >= B:
                min_gap = min(min_gap, abs(B-left), abs(B-right))
            elif left >= B:
                 min_gap = min(min_gap, abs(B-left))
            elif right >= B:
                min_gap = min(min_gap, abs(B-right))
            if min_gap == 0:
                endf = True
                break
        if endf:
            break
    print(f'#{tc} {min_gap}')