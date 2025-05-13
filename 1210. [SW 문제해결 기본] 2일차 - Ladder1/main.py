import sys

sys.stdin = open("input.txt", "r")

def find_route(arr, finish):
    x = finish
    y = 99

    visited = [[False]*100 for _ in range(100)]

    while y > 0:
        visited[y][x] = True

        # 왼쪽
        if x > 0 and arr[y][x-1] == 1 and not visited[y][x-1]:
            while x > 0 and arr[y][x-1] == 1 and not visited[y][x-1]:
                x -= 1
                visited[y][x] = True
        # 오른쪽
        elif x < 99 and arr[y][x+1] == 1 and not visited[y][x+1]:
            while x < 99 and arr[y][x+1] == 1 and not visited[y][x+1]:
                x += 1
                visited[y][x] = True
        # 위로 이동
        y -= 1

    return x

# 입력 및 실행
for tc in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if arr[99][i] == 2:
            ans = find_route(arr, i)
            print(f"#{T} {ans}")