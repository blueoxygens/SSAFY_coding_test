import sys
import math
from collections import defaultdict
import heapq

def dijkstra(graph, start):
    distances = {node: math.inf for node in graph}

    distances[start] = 0

    priority_queue = [(0,start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1,T+1):
    edges = list(map(int, input().strip().split(" ")))
    N = edges.pop(0)
    graph = defaultdict(dict)
    for i in range(N):
        for j in range(N):
            if edges[i*N+j] == 1:
                graph[i][j] = 1

    cc_values = []
    for i in range(N):
        cc_values.append(sum(dijkstra(graph, i).values()))
    
    print(f'#{tc} {min(cc_values)}')
    
    # for i in range(N):
    #     cc_values.append(sum(cc[i]))
    
    # print(f'#{tc} {min(cc_values)}')
#---------------------------------------------------------------
    # if tc == 1 : print(edges)
    # cc = [[0]*N for _ in range(N)]

    # for i in range(N):
    #     for j in range(N):
    #         if edges[i*N+j] != 0:
    #             cc[i][j] = edges[i*N+j]
    #         elif i != j:
    #             cc[i][j] = math.inf
    #         else:
    #             cc[i][j] = 0
    
    # floyd - warshall로 구현했으나 너무 느림. 다익스트라로 해야할듯
    # for k in range(N):
    # # i = 출발 노드
    #     for i in range(N):
    #         # j = 도착 노드
    #         for j in range(N):
    #             cc[i][j] = min(cc[i][j], cc[i][k] + cc[k][j])
    #             cc[j][i] = cc[i][j]
    
    # if tc == 1: print(cc)