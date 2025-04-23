import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1,T+1):
    k = int(input())
    students  = list(map(int, input().strip().split(" ")))
    result = 0
    #0, 2 / 0 
    for i in range(k):
        delete_list = []
        for j in range(0, pow(2,k)//pow(2,i), 2):
            result += (abs(students[j] - students[j+1]))
            #print(students)
            delete_list.append(min(students[j], students[j+1]))
            #print(students)
        for v in delete_list:
            students.remove(v)
    print(f'#{tc} {result}')