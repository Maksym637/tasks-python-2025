# Problem description: https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter


n = int(input())
shop_shoes = list(map(int, input().split()))

m = int(input())
desired_shoes = [tuple(map(int, input().split())) for _ in range(m)]

total_amount = 0
shoes_count = dict(Counter(shop_shoes))

for size, price in desired_shoes:
    if shoes_count.get(size, 0):
        total_amount += price
        shoes_count[size] -= 1

print(total_amount)
