n = int(input())
r1, c1, r2, c2 = input().split()
r1, c1, = int(r1), int(c1)
r2, c2, = int(r2), int(c2)

# 체스판 만들기
# coul = [0] * n
# row = []
# for i in range(n):
#     row.append(coul)
#print(row[0][2])

#이동

def move(r1, c1):
    count = 0
    while r1 != r2 or c1 != c2:
        #구할 수 없는 경우
        if (r1 + r2) % 2 == 1 :
            count = -1
            break

        # r1이 목표(r2)보다 클 때
        if r1 > r2:
            if c1 > c2:
                r1 = r1 - 2
                c1 = c1 - 1
                count += 1
            elif c1 < c2:
                r1 = r1 - 2
                c1 = c1 + 1
                count += 1
            elif c1 == c2 == 0:
                r1 = r1 - 2
                c1 = c1 + 1
                count += 1
            elif c1 == c2  == n:
                r1 = r1 - 2
                c1 = c1 - 1
                count += 1
            elif c1 == c2:
                r1 = r1 - 2
                c1 = c1 - 1
                count += 1

        # r1이 목표(r2)보다 작을 때
        if r1 < r2:
            if c1 > c2:
                r1 = r1 + 2
                c1 = c1 - 1
                count += 1
            elif c1 < c2:
                r1 = r1 + 2
                c1 = c1 + 1
                count += 1
            elif c1 == c2 == 0:
                r1 = r1 + 2
                c1 = c1 + 1
                count += 1
            elif c1 == c2  == n:
                r1 = r1 + 2
                c1 = c1 - 1
                count += 1
            elif c1 == c2:
                r1 = r1 + 2
                c1 = c1 - 1
                count += 1

        # r1이 목표(r2)와 같을 때
        if r1 == r2:
            if c1 > c2 and (c1 + c2) % 2 == 0:
                c1 = c1 - 2
                count += 1
            elif c1 < c2 and (c1 + c2) % 2 == 0:
                c1 = c1 + 2
                count += 1
            elif (c1 + c2) % 2 == 1:
                count = -1
                break
            #elif c1 < c2 and c2 - c1 == 1:
            #    c1 = c1 + 1
            #    count += 1
            #elif c1 > c2 and c1 - c2 == 1:
            #    c1 = c1 - 1
            #    count += 1
            #elif c1 == c1:
            #    break

    print(count)    


move(r1, c1)



