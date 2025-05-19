import sys
from collections import deque

def main():
    sys.stdin = open("input.txt","r")
    for tc in range(1,11):
        loop, boxes = int(input()), list(map(int, input().strip().split(" ")))
        count = len(boxes)-1

        for i in range (loop):
            #print(f'{boxes[count], boxes[0]}')
            boxes[count] -= 1
            boxes[0] += 1
            boxes.sort()
            if boxes[count] - boxes[0] <= 1:
                break
        print(f'#{tc} {boxes[count] - boxes[0]}')

if __name__ == '__main__':
    main()