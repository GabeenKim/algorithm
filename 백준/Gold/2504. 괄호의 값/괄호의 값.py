s = list(input())

result = []
count = 1
ans = 0

for i in range(len(s)):
    if s[i] == '[':
        result.append(s[i])
        count *= 3

    elif s[i] == '(':
        result.append(s[i])
        count *= 2

    elif s[i] == ']':
        if not result or result[-1] == '(':
            ans = 0
            break
        if s[i - 1] == '[':
            ans += count
        count //= 3
        result.pop()

    elif s[i] == ')':
        if not result or result[-1] == '[':
            ans = 0
            break
        if s[i - 1] == '(':
            ans += count
        count //= 2
        result.pop()

if result:
    ans = 0
print(ans)
