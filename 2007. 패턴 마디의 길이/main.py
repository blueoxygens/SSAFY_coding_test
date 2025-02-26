from collections import deque
import sys
sys.stdin = open("input.txt", "r")

def is_completed(arr, arr_compare):
    if arr[len(arr_compare):(len(arr_compare)*2)] == arr_compare:
        return True
    else:
        return False

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    temp = list(input().strip())
    queue = []
    deq = deque()
    for i in temp:
        deq.append(i)

    #큐 데크 스택
    while deq:
        queue.append(deq.popleft())
        if is_completed(temp, queue):
            break
    print(f'#{test_case} {len(queue)}')
