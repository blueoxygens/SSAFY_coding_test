#import sys
#sys.stdin = open("input.txt", "r")
 
def dfs(points_dict, points):
    if not points:
        return set([0])
    possible_scores = dfs(points_dict, points[1:])
    p = points[0]
    new_scores = set()
    for pp in range(0, points_dict[p]*p+1, p):
        new_scores = new_scores.union(set([x + pp for x in possible_scores]))
    possible_scores = possible_scores.union(set(new_scores))
    return possible_scores
 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    points_list = list(map(int, input().split()))
     
    points_set = set(points_list)
    points_dict = {x: points_list.count(x) for x in points_set}
     
    scores = dfs(points_dict, list(points_set))
     
    print(f"#{test_case} {len(scores)}")