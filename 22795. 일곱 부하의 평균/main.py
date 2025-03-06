import sys

sys.stdin = open("1_sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    six_dwarves = list(map(int, input().strip().split()))

    max_height = max(six_dwarves)
    total_height = sum(six_dwarves)

    # 사라진 부하의 키는 (전체 키 합이 7의 배수가 되도록 만드는 최소의 값)
    missing_height = max_height + 1
    total_height += missing_height

    while True:
        if total_height % 7 == 0:
            break
        total_height += 1
        missing_height += 1
    
    print(missing_height)
