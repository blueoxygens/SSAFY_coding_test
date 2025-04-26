import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().strip().split(" ")))
    if arr[0] >= 10 or arr[1] >= 10:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {arr[0]* arr[1]}')