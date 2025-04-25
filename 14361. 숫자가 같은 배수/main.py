import sys
from collections import Counter

sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    num = input().strip()
    original_counter = Counter(num)
    flag = False

    for i in range(2, 10**6):
        multiplied = str(int(num) * i)
        if len(multiplied) > len(num):
            break
        if Counter(multiplied) == original_counter:
            print(f"#{tc} possible")
            flag = True
            break

    if not flag:
        print(f"#{tc} impossible")
