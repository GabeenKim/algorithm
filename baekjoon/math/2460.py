result = 0
max_num = 0
for _ in range(10):
    a, b = map(int,input().split())
    result -= a
    if result <= 0 :
        result = 0
    result += b
    if max_num < result :
        max_num = result 

print(max_num)
