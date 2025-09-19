import sys

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    
    # 1. 200개의 복도 구간을 나타내는 리스트를 0으로 초기화
    corridor = [0] * 200 
    
    for _ in range(N):
        f, t = map(int, input().split())
        
        # 2. 방 번호를 복도 번호로 변환
        # (1,2)->0, (3,4)->1, ...
        start = (f - 1) // 2
        end = (t - 1) // 2
        
        # 3. start가 end보다 클 경우, 두 값을 바꿔줌 (항상 작은 쪽에서 큰 쪽으로 순회하기 위함)
        if start > end:
            start, end = end, start
            
        # 4. 해당 이동 경로가 지나는 모든 복도 구간의 카운트를 1씩 증가
        for i in range(start, end + 1):
            corridor[i] += 1
            
    # 5. 복도 구간에 쌓인 카운트 중 최댓값이 정답
    max_count = 0
    for count in corridor:
        if count > max_count:
            max_count = count
            
    # max() 함수를 사용하면 더 간단합니다: max_count = max(corridor)
    
    print(f'#{tc} {max_count}')