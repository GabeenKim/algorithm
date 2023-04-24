from itertools import combinations

array = [int(input()) for _ in range(9)]

#해당 배열을 7명 중복없이 뽑아줌.
for i in combinations(array,7):
    if sum(i) == 100 :
        for j in sorted(i):
            print(j)
        break

