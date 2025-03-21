import sys

sys.stdin = open("1_sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    player_num = int(input())
    A = list(map(int, input().strip().split(" ")))
    B = list(map(int, input().strip().split(" ")))
    selected_player = ['']*player_num
    selected_num = 0

    while selected_num < player_num:
        min = player_num
        index = 0
        for i, p in enumerate(A):
            if p <= min and not selected_player[i]:
                min = p
                index = i
        selected_player[index] = 'A'
        selected_num += 1
        if selected_num == player_num:
            break

        min = player_num
        index = 0
        for i, p in enumerate(B):
            if p <= min and not selected_player[i]:
                min = p
                index = i
        selected_player[index] = 'B'
        selected_num += 1
        if selected_num == player_num:
            break
    
    print(f'{''.join(selected_player)}')