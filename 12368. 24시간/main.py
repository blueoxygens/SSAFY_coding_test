import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    times = list(map(int, input().strip().split(" ")))
    print(f'#{tc} {(times[0]+times[1])%24}')