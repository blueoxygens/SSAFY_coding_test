import sys

sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    original = list(input().strip().split(" "))
    M = int(input())
    command = list(input().strip().split("I "))
    command = list(filter(None, command))
    for i in range(M):
        temp = list(map(int, command[i].strip().split(" ")))
        original = original[:temp[0]]+temp[2:]+original[temp[0]:]
    

    print(f'#{tc}', end = ' ')
    for i in range(10):
        print(int(original.pop(0)), end=' ')
    print()