import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    days = int(input())  # 매매가를 알고 있는 날짜의 수
    prices = list(map(int, input().strip().split()))  # 매매가 리스트

    max_price = 0  # 현재까지의 최대 매매가
    profit = 0  # 총 이익

    # 뒤에서부터 순회하면서 최대 매매가 갱신
    for price in reversed(prices):
        if price > max_price:
            max_price = price  # 최대값 갱신
        else:
            profit += (max_price - price)  # 현재 가격이 작다면 이익 추가

    print(f'#{test_case} {profit}')