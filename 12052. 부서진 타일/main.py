import sys

def is_broken(character):
    if character == '.':
        return False
    else:
        return True

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    row,  col = map(int, input().strip().split(" "))
    arr = []
    for i in range(row):
        arr.append(list(input().strip()))
    endf = False
    for i in range(row-1):
        for j in range(col-1):
            target = arr[i][j]
            if not is_broken(target):
                continue
            else:
                if is_broken(arr[i][j+1]) and is_broken(arr[i+1][j+1]) and is_broken(arr[i+1][j]):
                    target = '.'
                    arr[i][j+1] = '.'
                    arr[i+1][j] = '.'
                    arr[i+1][j+1] = '.'
                else:
                    endf = True
                    break
        if endf:
            break
    for i in range(row):
        if arr[i][col-1] == '#':
            endf = True
    if endf or '#' in arr[row-1]:
        print(f'#{test_case} NO')
    else:
       print(f'#{test_case} YES')