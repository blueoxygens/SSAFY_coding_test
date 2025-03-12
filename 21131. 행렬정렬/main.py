import sys

sys.stdin = open("1_sample_input.txt", "r")


#N*N 이하의 자연수 서로 다른 행렬
#A[i,j] // 정렬되었다는 것 => A[i,j] = (i -1) * N + j
# 1<= X <= N
#전체 행렬의 부분 행렬을 전치시킨다. X * X

def transpose(arr, X):
    new_arr = arr
    for row in range(X):
        for col in range(row,X):
            new_arr[row][col], new_arr[col][row] = arr[col][row], arr[row][col]
    return new_arr

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = []
    count = 0
    for i in range(N):
        arr.append(list(map(int, input().strip().split(" "))))
    for col in range(1,N):
        if col < N-1 and (arr[0][col]+1 != arr[0][col+1] and arr[0][col]+N != arr[0][col+1]):
            arr = transpose(arr, col)
            count += 1
            #print(f'condition 1 {arr}')
        elif col == N-1 and arr[0][N-1] != N:
            arr = transpose(arr, col)
            count+=1
            #print(f'condition 2 {arr}')
    print(f'{count}')
