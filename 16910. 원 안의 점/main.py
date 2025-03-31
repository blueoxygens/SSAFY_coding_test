import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    limit = pow(N, 2)
    count = 0

    for i in range (N+1):
        for j in range (N+1):
            x_2 = pow(i,2)
            y_2 = pow(j,2)
            if x_2 + y_2 <= limit:
                count += 1
    
    answer = count * 4 + 1 - 4*(N+1)
    print(f'#{test_case} {answer}')