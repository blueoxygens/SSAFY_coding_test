import sys
from collections import deque

sys.stdin = open("sample_input.txt", "r")

def find_S_in_E(S, E, pivots):
    if len(S) == 1:
        for i, w in enumerate(E, 0):
            if w == S[0]:
                pivots.append([i, i])
    else:
        #case 1 찾기
        for i, w in enumerate(E, 0):
            if w == S[0]:
                for si in range(1, len(S)):
                    if i+si >= len(E) or E[i+si] != S[si]:
                        break
                    elif si == len(S)-1:
                        pivots.append([i, i+si])
    #case 2 찾기 인덱스 계산 개선해야함.
        for i, w in enumerate(E[::-1], 0):
            if w == S[0]:
                for si in range(1, len(S)):
                    if i+si >= len(E) or E[i+si] != S[si]:
                        break
                    elif si == len(S)-1:
                        pivots.append([i-len(S), i+si-len(S)])
#0123
#-4-3-2-1

def find_possibility(S,E,pivots):
    for pivot in pivots:
        if pivot[0] >= 0 and pivot[1] + 1 != len(E):
            front = deque(E[0:pivot[0]])
            rear = deque(E[pivot[1]+1:])

        elif pivot[0] >= 0:
            front = deque(E[0:pivot[0]])

        elif abs(pivot[1]) != len(E):
            front = deque(E[-1:pivot[0]])
            rear = deque(E[pivot[1]-1:])

        else:
            front = deque(E[-1:pivot[0]])
            
        

T = int(input())
for test_case in range(1, T+1):
    S = list(input().strip())
    E = list(input().strip())
    pivots = []
    #두 가지 연산 S의 뒤에 X 붙이기 S = put_str(S, 'X')
    #S를 뒤집은 다음 제일 뒤에 Y 붙이기 S = put_str(S[::-1], 'Y')
    #위 두 연산을 적절히 활용하면 S == E가 될 수 있는가?
    '''음.. 그니까 E_list에서 S를 찾는다.
    case 1. 그냥 S가 E_list 안에 포함
    -> 처음 index와 끝 index를 기록, 그걸로 분할, stack에 저장. Y의 개수는 총 짝수개여야 함. 
    case 2. reversed S가 E_list 안에 포함
    _> 처음 index와 끝 index를 기록, 그걸로 분할, stack에 저장. Y의 개수는 총 홀수개여야 함.
    
    #num Yes, No 형식
    '''
    '''find_S_in_E(S, E, pivots)
    if not pivots:
        print(f'#{test_case} No')
    elif find_possibility(S, E, pivots):
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')'''
    #print(pivots)
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