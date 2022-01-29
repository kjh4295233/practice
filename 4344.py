n = int(input())

#정답 보관함
jae = []

for i in range(n):
    cnt = 0
    total_score = 0
    try_score = list(map(int,input().split()))
    
    # total score
    for j in range (1, try_score[0] + 1):
        total_score += try_score[j]
    
    # count over avg
    for k in range (1, try_score[0] + 1):
        if try_score[k] > total_score / try_score[0]:
            cnt += 1
        else:
            pass
                
    ans = (cnt/try_score[0]*100)
    jae.append(ans)

for i in range(n):
    print(f"{jae[i]:.3f}%")
    #print("{:.3f}%".format(jae[i]))

   




