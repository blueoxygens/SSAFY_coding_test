import sys

sys.stdin = open("input.txt", "r")

T = int(input())
 
for test_case in range(1, T+1):
    tc = int(input())
    arr  = list(map(int, input().strip().split(" ")))
    count_arr = [0]*101
     
    for n in arr:
        count_arr[n] += 1
    max = sorted(count_arr).pop()
    #print(max)
    answer = 0
    for i, n in enumerate(count_arr):
        if n == max and i > answer:
            answer = i
    print(f'#{tc} {answer}')