import sys

cities = int(sys.stdin.readline())
roads = list(map(int,sys.stdin.readline().split()))
price = list(map(int,sys.stdin.readline().split()))

answer_list = [0] * (cities-1)

for i in range(1, cities):
    answer_list[i-1] = roads[i-1] * price[i-1]

    if price[i-1] <= price[i]:
        price[i] = price[i-1]

answer = sum(answer_list)
print(answer)

