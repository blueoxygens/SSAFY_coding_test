import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f'#{test_case}')
    num = int(input())
    arr = [[0]*num for _ in range(num)]
    for i in range(num): #행 이동
        for j in range(i+1):#열 이동
            if j == 0 or j == (num-1):
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
    for i in range(num): #행 이동
        for j in range(i+1):#열 이동
            if j != i:
                print(f'{arr[i][j]}', end=' ')
            else:
                print(arr[i][j])