a, b = map(int, input().split())

arr = [1]
sum = 0
for i in range(2, 46):
    for j in range(i):
        arr.append(i)

pre_fix = [0]
for i in arr:
    sum += i
    pre_fix.append(sum)

print(pre_fix[b] - pre_fix[a - 1])
