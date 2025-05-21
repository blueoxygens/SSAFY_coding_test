import sys
from collections import deque

sys.stdin = open("input.txt", "r")

for tc in range(1,11):
    data_len, start = map(int,input().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    fnode = []
    tnode = []
    for i in range(0,data_len,2):
        fnode.append(arr[i])
        tnode.append(arr[i+1])
    visited = set()
    visited.add(start)
    clv = deque()
    clv.append(start)
    nlv = []
    plv = []

    while clv or nlv:
        node = clv.popleft()
        plv.append(node)
        for i in range(data_len//2):
            if fnode[i] == node and tnode[i] not in visited and tnode[i] not in nlv:
                nlv.append(tnode[i])
                visited.add(tnode[i])
        #현재 lv의 노드에 연결된 노드를 방문하지 않았고 다음 레벨 리스트에 없다면 다음 레벨에 추가
        if not clv and nlv:
            plv = []
            clv = deque(nlv)
            nlv = []
        #현재 레벨을 모두 방문했고 다음 레벨 리스트가 비어있지 않으면 과거 레벨 리스트, 다음 레벨 리스트 초기화
    print(f'#{tc} {max(plv)}')