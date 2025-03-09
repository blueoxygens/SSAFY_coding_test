import sys

sys.stdin = open("1_sample_input.txt", "r")

def client(L, R):
   if L < (R + 1) / 2:
        print('no')
   else:
    print('yes')

T = int(input())

for test_case in range(1, T + 1):
   '''
    고객은 N/X 개를 묶음 세트로 구매, N mod X 개를 단품으로 구매
    단, N mod X가 2/X 이상일 경우 묶음 세트를 하나 더 구매
    L개 이상 R개 이하의 음료수를 구매하고 싶다는 것을 알게되었다.
    L <= N <= R 단제품 대신 묶음 세트를 하나 더 구매하는 자연수 X가 있는가?
   '''
   LR = list(map(int, input().strip().split(" ")))
   client(LR[0], LR[1])