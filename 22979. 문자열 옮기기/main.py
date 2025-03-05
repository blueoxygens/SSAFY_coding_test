import sys
from collections import deque
sys.stdin = open("1_sample_input.txt", "r")

def move_string(str, s):
    if s > 0:
        for _ in range(s):
            str.append(str.popleft())
    elif s < 0:
        for _ in range(-s):
            str.appendleft(str.pop())
    else:
        return
        
def slicing(text, s):
    if not text:  # 빈 문자열 예외 처리
        return ""

    length = len(text)
    s = s % length  # s가 문자열 길이를 초과할 경우 처리

    if s > 0:
        return text[s:] + text[:s]  # 왼쪽으로 s칸 이동
    elif s < 0:
        return text[s:] + text[:s]  # 오른쪽으로 |s|칸 이동
    else:
        return text  # s가 0이면 그대로 반환


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # X>0 S의 첫 글자를 떼네어 마지막 글자 뒤에 붙이는 작업 X회
    # X<0 S의 마지막 글자를 떼네어 첫 번째 글자 앞에 붙이는 작업을 -X회
    # X=0 아무 일도 일어나지 X

    #deque 사용해서 연산처리 해봤는데 제한 시간 초과..
    #아마 인덱스 연산으로 처리해야할듯..?
    dq = deque(input())
    #print(dq)
    repeat_time = int(input())
    #print(repeat_time)
    S = input().strip().split(" ")
    #print(S)
    '''for i in range(repeat_time):
        move_string(dq, int(S[i]))'''
    for i in range(repeat_time):
        dq = slicing("".join(dq), int(S[i]))
    print("".join(dq))
    #print(str(dq))