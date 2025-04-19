#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A_len, B_len = map(int, input().strip().split(" "))
    A = set(list(map(int, input().strip().split(" "))))
    B = set(list(map(int, input().strip().split(" "))))
    #print(f'{A} / {B}')
    count = 0
    for i in A:
        if i in B:
            count += 1
    print(f'#{test_case} {count}')