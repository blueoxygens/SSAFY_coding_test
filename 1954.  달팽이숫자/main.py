import sys
sys.stdin = open("input.txt", "r")

def moveright():
    print('moved')
    #오른쪽으로 이동
    
def moveup():
    print('moved')
    #위쪽으로 이동
    
def moveleft():
    print('moved')
    #왼쪽으로 이동
    
def movedown():
    print('moved')
    #아래쪽으로 이동
    
def command_index_changer(command_index):
    command_index += 1
    command_index = command_index % 4
    return command_index
#command_index 변환기

T = int(input())
for test_case in range(1, T + 1):

  directions = ['right', 'down', 'left', 'up']
  N = int(input())
  arr = [[0]*N for _ in range(N)]
  command_index = 0 #command index
  row_index = 0
  col_index = 0

  for num in range (1,N+1):
    if directions[command_index] == 'right':
        moveright()
    elif directions[command_index] == 'down':
        movedown()
    elif directions[command_index] == 'left':
        moveleft()
    elif directions[command_index] == 'up':
        moveup()
    arr[row_index][col_index] = num

  print(f'#{test_case}')

  for r in range (N) :
    for c in range (N) :
        if c == N-1:
            print(arr[r][c])
        else:
            print(arr[r][c], end=' ')