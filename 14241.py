n = int(input())
size = list(map(int,input().split()))
score = 0

size.sort()

if len(size) == 2:
    score = size[0] * size[1]
    print(score)
else:
    while len(size) > 2:
    #if len(size) > 2:
        for i in range(n):
            score = score + size[0] * size[1]
            size[0] = size[0] + size[1]
            del size[1]
            size.sort()
            if len(size) == 2:
                score = score + size[0] * size[1]
                break
            else:
                continue
    print(score)
        


# from functoos import reduce
# print(reduce(lambda x, y: x+y, [1,2,3,4,5]))

#리스트 앞에 두 개 더한걸 리스트 첫 번째 값으로 저장, 자연스럽게 세 번째 값을 두 번째 값으로.