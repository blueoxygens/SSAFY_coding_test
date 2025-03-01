import gc
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    temp = input()
    M, N = int(temp.strip().split(" ")[0]), int(temp.strip().split(" ")[1])
    #M은 파리의 개수 배열의 한 변의 크기, N은 파리채의 한 변의 크기 
    del temp
    gc.collect()
    #print(f'{M} {N}')
    arr = [[0]*M for _ in range(M)] #파리의 개수 저장 배열
    for i in range(M):
        temp = input().strip().split(" ")
        for j in range(M):
            arr[i][j] = int(temp[j])
    #print(arr)
    Max = 0
    for i in range(M-N+1):
        for j in range(M-N+1):
            temp = 0
            for k in range(i,i+N):
                for v in range(j, j+N):
                    temp += arr[k][v]
            if temp > Max:
                Max = temp
    print(f'#{test_case} {Max}')