import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

'''
동전을 던졌을 때 앞면이 나오면 왼-가운데 컵 교환, 뒷면이 나오면 오른-가운데 컵 교환 (확률 50%)
방울이 들어있는 컵을 교환 시 방울이 한 번씩 울린다.
이때, 방울이 들어있을 확률이 가장 큰 컵의 위치는? 
'''

for test_case in range(1,T+1):
    arr = list(map(str,input().strip().split(" ")))
    bell_ringed = int(arr[1])
    current_bell_location = 0

    for i, s in enumerate(arr[0], 0):
        if s == 'o':
            current_bell_location = i
    
    if bell_ringed == 0:
        print(f'#{test_case} {current_bell_location}')
    elif current_bell_location == 1:
        #흠 운빨 게임 아닌가 아 여러 개가 있으면 가장 왼쪽
        #case 1. 원래 방울 위치가 가운데일 때
        if bell_ringed % 2 == 0:
            print(f'#{test_case} {current_bell_location}')
        else:
            print(f'#{test_case} 0')
    else:
        #case 2. 원래 방울 위치가 사이드일 때
        if bell_ringed % 2 == 0:
            print(f'#{test_case} 0')
        else:
            print(f'#{test_case} 1')