import sys
from collections import Counter

sys.stdin = open("2_sample_input.txt", "r")

T = int(input())

for tc in range(T):
    N = int(input())
    inputA = [list(map(int, input().split(" "))) for _ in range(2*N)]

    if N == 1:
        print(inputA[0][0])
        continue

    A = [0]*N
    At = [[0]*N for _ in range(N)]

    #첫 요소 알아냄
    temp = []
    for j in range(2*N):
        temp.append(inputA[j][0])
    counter = Counter(temp)
    A[0] = counter.most_common(1)[0][0]
    # 첫 row 알아냄
    for row in inputA:
        if row[0] == A[0]:
            for i in range(1, N):
                A[i] = row[i]
            break
    
    for index, element in enumerate(A):
        for i in range(2*N):
            if inputA[i][0] == element:
                if index != 0:
                    for j in range(N):
                        At[index][j] = inputA[i][j]
                    break
                elif N > 1 and inputA[i][1] != A[index+1]:
                    for j in range(N):
                        At[index][j] = inputA[i][j]
                    break    

    for i in range(N):
        for j in range(i,N):
            At[i][j], At[j][i] = At[j][i], At[i][j]
    
    for row in At:
        for element in row:
            print(element, end=" ")
        print()