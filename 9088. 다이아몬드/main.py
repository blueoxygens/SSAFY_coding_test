import sys

sys.stdin = open("sample_input.txt", "r")

TC = int(input())

for T in range(1, TC+1):
    N, K = map(int, input().strip().split(" "))
    arr = []
    for i in range(N):
        arr.append(int(input()))

    arr = sorted(arr)
    l = len(arr)
    max = 0
    for i in range(l, 0, -1):
        for j in range(l-1):
            if j + i > l-1 :
                break
            if arr[j+i]-arr[j] > K:
                break
            if i > max:
                max = i
    print(f'#{T} {max+1}')

#맞는지 틀린지 확인 불가