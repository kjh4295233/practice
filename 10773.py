import sys

num = []
n = int(sys.stdin.readline())
for i in range(n):
    ans = int(sys.stdin.readline())
    if ans != 0:
        num.append(ans)
    elif ans == 0:
        del(num[-1])

print(sum(num))
