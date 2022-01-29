#trees) 4 3 3 2
#day 1) 4
#day 2) 3 3
#day 3) 2 2 3 
#day 4) 1 1 2 2

#day 5) 0 0 1 1
#day 6) 0 0 0 0
#day 7) 초대

# n = 묘목
# t = 시간

n = int(input())

tim_l = list(map(int,input().split()))
tim_l.sort(reverse = True)
print(tim_l)
fin_day = []

for i in range(n):
    d = tim_l(i) - (n - i)
    fin_day.append(d)
print(tim_l)

