import sys

def check_condition(arr):
    if arr[0] < arr[1] and arr[1] < arr[2]:
        return True
    return False

def main():
    sys.stdin = open("sample_input.txt", "r")

    T = int(input())

    for tc in range(1,T+1):
        candies = list(map(int, input().split(" ")))
        print(candies)
        if check_condition(candies):
            print(f'#{tc} 0')
        else:
            first = candies[0]
            second = candies[1]
            third = candies[2]
            gap1, gap2 = 0, 0
            if second >= third:
                gap1 = abs(third - second) + 1
                second -= gap1
            if first >= second:
                gap2 = abs(second - first) + 1
                first -= gap2
            if first > 0 and second > 0:
                print(f'#{tc} {gap1 + gap2}')
            else:
                print(f'#{tc} -1')


if __name__ == '__main__':
    main()