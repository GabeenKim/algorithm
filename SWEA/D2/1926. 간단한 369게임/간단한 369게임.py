N = int(input())
ans = []
for i in range(1, N+1):
    num = str(i)
    if '3' in num or '6' in num or '9' in num:
        cnt = 0
        cnt += num.count('3')
        cnt += num.count('6')
        cnt += num.count('9')
        ans.append('-'*cnt)
    else:
        ans.append(num)
print(*ans)