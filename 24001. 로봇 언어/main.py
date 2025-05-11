import sys
sys.stdin = open("1_sample_input.txt", "r")

T = int(input())

for _ in range(T):
    s = input().strip()
    min_pos = 0
    max_pos = 0
    max_distance = 0

    for ch in s:
        if ch == 'L':
            min_pos -= 1
            max_pos -= 1
        elif ch == 'R':
            min_pos += 1
            max_pos += 1
        else:  # '?'
            # 확장 가능: 왼쪽으로 한 번, 오른쪽으로 한 번
            next_min = min(min_pos - 1, max_pos - 1)
            next_max = max(min_pos + 1, max_pos + 1)
            min_pos, max_pos = next_min, next_max

        max_distance = max(max_distance, abs(min_pos), abs(max_pos))

    print(max_distance)
