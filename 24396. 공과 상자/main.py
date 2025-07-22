import sys
from collections import deque

sys.stdin = open("1_sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    b, w, x, y, z = map(int, input().strip().split(" "))
    #b개의 검은 공, 상자
    #w개의 흰 공, 상자
    #검-검 x점, 흰-흰 y점, 섞이면 z점
    score = 0
    if z > x and z > y:
        # score += z*min(b, w), score += x*
        min_ball = min(b, w)
        score += z*min_ball*2
        score += x*abs(b-min_ball)
        score += y*abs(w-min_ball)
    else:
        min_ball = min(b, w)
        score += x*abs(b-min_ball)
        score += y*abs(w-min_ball)
    print(score)