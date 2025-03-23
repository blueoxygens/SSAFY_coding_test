import sys

def find_duplicate (arr, value, pivot):
    count = 0
    result = []
    for i, v in enumerate(arr):
        if v == value:
            count += 1
            result.append(i)
    result = result[::-1][:pivot][::-1]
    return result

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    #arr, 횟수
    arr, num = input().strip().split(" ")
    arr = list(map(int,list(arr)))
    num = int(num)
    sorted_arr = sorted(arr)[::-1]
    #print(f'{sorted_arr}, {num}')
    '''
    최대값이 index 0에 가깝게 가야한다.
    index가 겹치는 경우
    reversed arr
    '''
    for time in range(num):
        checked = False
        for i in range(len(arr)):
            if arr == sorted_arr:
                checked = True
                arr[-1], arr[-2] = arr[-2], arr[-1]
            elif arr[i] != sorted_arr[i] :
                index_arr = find_duplicate(arr, sorted_arr[i], num)
                if len(index_arr) > 1:
                    checked = True
                    arr[index_arr[time]], arr[i] = arr[i], arr[index_arr[time]]
                else:
                    checked = True
                    arr[index_arr[0]], arr[i] = arr[i], arr[index_arr[0]]
            if checked:
                break
    arr = "".join(list(map(str,arr)))
    print(f'#{test_case} {arr}')