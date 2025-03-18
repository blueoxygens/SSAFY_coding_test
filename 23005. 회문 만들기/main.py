import sys

sys.stdin = open("2_sample_input.txt","r")

t = int(input())
 
for tc in range(1, t+1):
    s = input().rstrip()
 
    i, j = 0, len(s) - 1
 
    count = 0
    while i < j:
        if s[i] == s[j]:
            i, j = i + 1, j - 1
            continue
         
        # 앞에 문자가 'x'인 경우, x 우측에 삽입
        elif s[i] == "x":
            count += 1
            i += 1
 
        elif s[j] == "x":
            count += 1
            j -= 1
 
        else: break
 
    if i >= j: print(count)
    else: print(-1)
