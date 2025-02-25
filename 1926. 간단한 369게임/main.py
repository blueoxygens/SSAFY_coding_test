import sys
sys.stdin = open("input.txt", "r")

T = int(input())

compare_arr = [3,6,9]

def determine_num(num):
    if num in compare_arr:
        return True
    else:
        return False

for test_case in range(1, T + 1):
    if test_case == 1000:
        print(test_case)
    elif test_case >= 100:
        if determine_num(test_case//100) and determine_num((test_case%100)//10) and determine_num((test_case - test_case//100*100 - (test_case%100)//10*10)):
            print('---', end='')
        elif (determine_num(test_case//100) and determine_num((test_case%100)//10)) or (determine_num((test_case%100)//10) and determine_num((test_case - test_case//100*100 - (test_case%100)//10*10))) or (
            determine_num(test_case//100) and determine_num((test_case - test_case//100*100 - (test_case%100)//10*10))
        ):
            print('--', end='')
        elif determine_num(test_case//100) or determine_num((test_case%100)//10) or determine_num((test_case - test_case//100*100 - (test_case%100)//10*10)):
            print('-', end='')
        else:
            print(test_case, end='')
    elif test_case >= 10:
        if determine_num(test_case//10) and determine_num((test_case - test_case//10*10)):
            print('--', end='')
        elif determine_num(test_case//10) or determine_num((test_case - test_case//10*10)):
            print('-', end='')
        else:
            print(test_case, end='')
    else:
        if determine_num(test_case):
             print('-', end='')
        else:
            print(test_case, end='')
    if test_case < T:
            print(' ', end='')