import sys

delta = [[0, 1], [1, 0], [-1, 0], [0, -1]]  # 우 하 상 좌
arrows = {
    '<': 3,
    '>': 0,
    '^': 2,
    'v': 1,
}


def next_x(x):
    return x % R


def next_y(y):
    return y % C


def go(nx, ny, val, drt):
    global result, func_stop, check_stop

    now = command[nx][ny]
    key = str(nx) + str(ny) + str(val) + str(drt)
    # 최대 재귀 깊이 이상으로 호출되는 것을 막기 위함
    if key in visited:
        return
    else:
        visited.append(key)
    # @를 발견한 이후의 함수 호출에 대해서는 바로 바로 리턴 -> 실행시간 1/4로 감소
    if check_stop:
        return

    if now == '@':
        result = 'YES'
        check_stop = True
        return
    elif now == '.':
        go(next_x(nx + delta[drt][0]), next_y(ny + delta[drt][1]), val, drt)
    elif now in arrows:
        go(next_x(nx + delta[arrows[now]][0]), next_y(ny + delta[arrows[now]][1]), val, arrows[now])
    elif now == '_':
        if val == 0:
            go(next_x(nx + delta[0][0]), next_y(ny + delta[0][1]), val, 0)
        else:
            go(next_x(nx + delta[3][0]), next_y(ny + delta[3][1]), val, 3)
    elif now == '|':
        if val == 0:
            go(next_x(nx + delta[1][0]), next_y(ny + delta[1][1]), val, 1)
        else:
            go(next_x(nx + delta[2][0]), next_y(ny + delta[2][1]), val, 2)
    elif now == '?':
        for i in range(4):
            go(next_x(nx + delta[i][0]), next_y(ny + delta[i][1]), val, i)
    elif now == '+':
        go(next_x(nx + delta[drt][0]), next_y(ny + delta[drt][1]), (val + 1) % 16, drt)
    elif now == '-':
        go(next_x(nx + delta[drt][0]), next_y(ny + delta[drt][1]), (val - 1 + 16) % 16, drt)
    else:
        go(next_x(nx + delta[drt][0]), next_y(ny + delta[drt][1]), int(now), drt)

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    R, C = map(int, input().split())
    command = [input() for _ in range(R)]
    visited = []
    result = 'NO'
    check_stop = False
    func_stop = False

    keyx, keyy = 0, 0
    for row in range(R):
        if '@' in command[row]:
            for col in range(C):
                if command[row][col] == '@':
                    keyx = row
                    keyy = col
            check_stop = True
            break

    # tc 40 처리: @가 화살표로 둘러싸여서 접근할 수 없으면 함수 호출 안 함
    limit = 0
    check = 0
    for d in delta:
        cx = keyx + d[0]
        cy = keyy + d[1]
        if 0 <= cx < R and 0 <= cy < C:
            limit += 1
            if command[cx][cy] in arrows:
                check += 1
    if check_stop and limit != check:
        check_stop = False
        go(0, 0, 0, 0)

    print('#{} {}'.format(tc, result))