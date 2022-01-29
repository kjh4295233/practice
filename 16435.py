fruit, long = input().split()
fruit, long = int(fruit), int(long)

trees = list(map(int,input().split()))
trees.sort()
#print(trees)

for i in range(fruit):
    if long >= trees[i]:
        long += 1
    else:
        break
print(long)

# github 연습용 수정