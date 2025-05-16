import sys
def is_palindrome(string):
    str_len = len(string)
    front = string[0:str_len//2]
    rear = string[-1:-1*(str_len//2)-1:-1]
    #print(f'{front} {rear}')
    if front == rear:
        return True
    else:
        return False

def main():
    sys.stdin = open("sample_input.txt", "r")

    T = int(input())

    for tc in range(1, T+1):
        #print(input())
        input_str = list(input())
        if is_palindrome(input_str):
            if is_palindrome(input_str[0:len(input_str)//2]) and is_palindrome(input_str[len(input_str)//2+1:]):
                print(f'#{tc} YES')
            else:
                print(f'#{tc} NO')
        else:
            print(f'#{tc} NO')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
