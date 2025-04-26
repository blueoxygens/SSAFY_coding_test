import sys

sys.stdin = open("2_sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    white = list(map(int, input().split()))
    black_one = list(map(int, input().split()))
    black_two = list(map(int, input().split()))

    # 흰 종이 영역
    wx1, wy1, wx2, wy2 = white

    # 흰 종이 안에서 검은 종이가 덮는 부분 계산
    # 첫 번째 검은 종이와 겹치는 영역
    bx1 = max(wx1, black_one[0])
    by1 = max(wy1, black_one[1])
    bx2 = min(wx2, black_one[2])
    by2 = min(wy2, black_one[3])

    # 두 번째 검은 종이와 겹치는 영역
    cx1 = max(wx1, black_two[0])
    cy1 = max(wy1, black_two[1])
    cx2 = min(wx2, black_two[2])
    cy2 = min(wy2, black_two[3])

    # 겹치는 부분이 실제로 존재하는지 확인
    black_areas = []
    if bx1 < bx2 and by1 < by2:
        black_areas.append((bx1, by1, bx2, by2))
    if cx1 < cx2 and cy1 < cy2:
        black_areas.append((cx1, cy1, cx2, cy2))

    # 덮인 영역을 계산
    # 만약 두 영역이 서로 겹치면, 합쳐서 봐야 함
    covered_area = 0

    # 검은 종이 1 면적
    if bx1 < bx2 and by1 < by2:
        covered_area += (bx2 - bx1) * (by2 - by1)
    # 검은 종이 2 면적
    if cx1 < cx2 and cy1 < cy2:
        covered_area += (cx2 - cx1) * (cy2 - cy1)

    # 두 검은 종이가 겹치는 부분 빼기 (겹치는 면적만큼 두 번 더해졌으니까)
    ix1 = max(bx1, cx1)
    iy1 = max(by1, cy1)
    ix2 = min(bx2, cx2)
    iy2 = min(by2, cy2)
    if ix1 < ix2 and iy1 < iy2:
        covered_area -= (ix2 - ix1) * (iy2 - iy1)

    # 흰 종이 전체 면적
    white_area = (wx2 - wx1) * (wy2 - wy1)

    # 최종 비교
    if covered_area < white_area:
        print('YES')
    else:
        print('NO')
