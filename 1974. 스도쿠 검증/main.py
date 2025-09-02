import sys
from collections import Counter
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = []
    for i in range(9):
        arr.append(Counter(list(map(int, input().strip().split(" ")))))
   #print(arr)
    comp = [1,2,3,4,5,6,7,8,9]
    # ct = Counter(arr)
    for i in range(9):
        for j in comp:
            if arr[i][j] != 1:
                print(0)
    print(1)