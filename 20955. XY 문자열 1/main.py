import sys
from collections import deque

sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    S = list(input().strip())
    E = list(input().strip())

    #두 가지 연산 S의 뒤에 X 붙이기 S = put_str(S, 'X')
    #S를 뒤집은 다음 제일 뒤에 Y 붙이기 S = put_str(S[::-1], 'Y')
    #위 두 연산을 적절히 활용하면 S == E가 될 수 있는가?
    dq = deque(E)
    rflag = False
    while len(dq) != len(S):
        if rflag:
            temp = dq.popleft()
            if temp == 'Y':
                rflag = False
        else:
            temp = dq.pop()
            if temp == 'Y':
                rflag = True

    if list(dq) == S and not rflag:
        print(f'#{test_case} Yes')
    elif list(dq)[::-1] == S:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')