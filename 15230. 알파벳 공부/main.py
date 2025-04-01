import sys
from collections import deque

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    string = list(input())
    abc = list('abcdefghijklmnopqrstuvwxyz')
    dq1 = deque(string)
    dq2 = deque(abc)
    count = 0
    while dq1:
        if dq1.popleft() == dq2.popleft():
            count += 1
        else:
            break
    print(f'#{test_case} {count}')