'''
주머니의 개수 N, 나눠 줄 주머니의 개수 K
주머니 속 사탕의 개수
(최대값과 최솟값)차이의 최솟값
'''
import sys

sys.stdin = open("sin.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    N, K = map(int, input().strip().split(" "))
    candies = list(map(int, input().strip().split(" ")))
    candies.sort()
    #범위 왔다리 갔다리 하면서 최솟값 갱신 ㄱㄱ
    pivot = 0
    minimum = max(candies) -  min(candies)
    while pivot + K -1 < len(candies):
        if candies[pivot + K -1 ]-candies[pivot] < minimum:
            minimum = candies[pivot + K -1 ]-candies[pivot]
            pivot += 1
        else:
            pivot += 1
    print(f'#{test_case} {minimum}')