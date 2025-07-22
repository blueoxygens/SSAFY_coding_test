import sys
from collections import deque


def main():
    sys.stdin = open("Sample_input.txt", "r")

    T = int(input())

    for tc in range(1, T+1):
        N, length = map(int, input().strip().split(" "))
        arr = list(map(int, input().strip().split(" ")))
        to_len = [[0]*(length+1) for i in range(length+1)]
        answer = 999999999999999
        for i in arr:
            for j in arr:
                if i > j:
                    to_len[i][j] = length-(i-j)
                else:
                    to_len[i][j] = j - i
        to = 0
        fromn = 0
        max = 0
        temp = 0
        for i in arr:
            for j in arr:
               if max <to_len[i][j]:
                    max = to_len[i][j]
                    to = i
                    fromn = j
        must_visit = deque(arr[:to] + arr[to + 1:])
        before = 1
        while must_visit:
            current = must_visit.popleft()
            temp += to_len[before][current]
            before = current
        answer = min(answer, temp)
        print(f'#{tc} {answer}')



if __name__ == "__main__":

    main()