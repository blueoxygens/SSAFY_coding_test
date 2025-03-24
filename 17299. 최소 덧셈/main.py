import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    ab = input()
    min = int(ab)
    for i in range(1, len(ab)):
        a = int(ab[:i])
        b = int(ab[i:])
        if a+b < min:
            min = a+b
    print(f'#{test_case} {min}')