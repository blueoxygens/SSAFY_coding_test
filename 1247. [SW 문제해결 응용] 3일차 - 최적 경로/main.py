import sys
from collections import deque

sys.stdin = open("input.txt", "r")

def calc_distance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1 - y2)
    #----------------------------------------생각 좀 해보자------------------------------
    #회사, 집, 고객의 좌표

def dfs(current, nodes, distances, visited, total_distance, min_distance):
    # Base case: all nodes visited, return distance to home (index 1)
    if len(visited) == len(nodes):
        return total_distance + distances[current][1]
    
    # Initialize local minimum distance for this recursion
    local_min = float('inf')
    
    # Try visiting each unvisited node
    for node in nodes:
        if node not in visited:
            # Calculate new distance
            new_distance = total_distance + distances[current][node]
            # Prune if the current path is already longer than the known minimum
            if new_distance >= min_distance[0]:
                continue
            # Mark node as visited
            visited.add(node)
            # Recurse
            result = dfs(node, nodes, distances, visited, new_distance, min_distance)
            # Update minimum distance if a better path is found
            local_min = min(local_min, result)
            # Backtrack: remove node from visited
            visited.remove(node)
    
    return local_min

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    coordinates = list(map(int, input().strip().split(" ")))
    distances = [[0]*(N+2) for _ in range(N+2)]
    for i in range(N+1):
        for j in range(i, N+2):
            #0,2,4,6 // index * 2
            distance = calc_distance(coordinates[i*2], coordinates[i*2+1], coordinates[j*2], coordinates[j*2+1])
            distances[i][j] = distance
            distances[j][i] = distance
    #print(distances)
    nodes = list(range(2, N + 2))
    # Track visited nodes
    visited = set()
    # Track global minimum distance
    min_distance = [float('inf')]
    result = dfs(0, nodes, distances, visited, 0, min_distance)
    
    print(f"#{tc} {result}")