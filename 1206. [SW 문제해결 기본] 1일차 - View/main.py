import sys

sys.stdin = open("sample_input.txt", "r")

def check_avail(index, arr, num):
    if index + num < 0  or index + num >= len(arr):
        return False
    return True


for test_case in range(1, 11):
    #오른쪽 2칸, 왼쪽 2칸 체크
    buildings = int(input())
    arr = list(map(int, input().strip().split(" ")))
    answer = 0
    for i, b in enumerate(arr):
        min = 10000
        flag = False
        for index in range(-2, 3):
            if index ==0:
                continue
            if check_avail(i, arr, index):
                if arr[i] - arr[i + index] <= 0:
                    flag = True
                    break
                elif arr[i] - arr[i + index] < min:
                    min = arr[i] - arr[i + index]
        if not flag:
            answer += min
    print(f'#{test_case} {answer}')