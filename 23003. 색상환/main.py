import sys
sys.stdin = open("1_sample_input.txt", "r")

T = int(input())
color_arr = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

def get_color_relation(color1, color2):
    if color1 == color2:
        return 'E'
    if color1 not in color_arr or color2 not in color_arr:
        return 'X'
    
    idx1 = color_arr.index(color1)
    idx2 = color_arr.index(color2)
    
    if abs(idx1 - idx2) == 1 or abs(idx1 - idx2) == 5:
        return 'A'
    if abs(idx1 - idx2) == 3:
        return 'C'
    return 'X'

for test_case in range(1, T + 1):
    input_arr = input().strip().split()
    if len(input_arr) != 2:
        print('X')
    else:
        print(get_color_relation(input_arr[0], input_arr[1]))
