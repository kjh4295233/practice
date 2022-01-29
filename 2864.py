n1, n2 = input().split(" ")

small_n1 = n1.replace('6','5')
small_n2 = n2.replace('6','5')

big_n1 = n1.replace('5','6')
big_n2 = n2.replace('5','6')

small_n1, small_n2 = int(small_n1), int(small_n2)
big_n1, big_n2 = int(big_n1), int(big_n2)

small_sum = small_n1 + small_n2
big_sum = big_n1 + big_n2

print(small_sum, big_sum, end = ' ')
