#import sys
#sys.stdin = open("input.txt", "r")

def is_bigger(x, y, standard):
    return (x+y) > standard

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = input().strip().split(' ')
    count = 0
    while not is_bigger(int(arr[0]), int(arr[1]), int(arr[2])):
        if int(arr[1]) > int(arr[0]):
            arr[0] = int(arr[0]) + int(arr[1])
        else:
            arr[1] = int(arr[0]) + int(arr[1])
        count+=1
    count+=1
    print(count)