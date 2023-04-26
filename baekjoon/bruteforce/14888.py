#연산자 끼워넣기 _DFS이용 

n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = -int(1e9)
min_result = int(1e9)


def dfs(add, sub, mul, div, sum, idx):
    global max_result, min_result
    if idx == n:
        max_result = max(max_result, sum)
        min_result = min(min_result, sum)
        return

    if add:
        dfs(add - 1, sub, mul, div, sum + arr[idx], idx + 1)
    if sub:
        dfs(add, sub - 1, mul, div, sum - arr[idx], idx + 1)
    if mul:
        dfs(add, sub, mul - 1, div, sum * arr[idx], idx + 1)
    if div:
        dfs(add, sub, mul, div - 1, int(sum /arr[idx]), idx + 1)


dfs(add, sub, mul, div, arr[0], 1)

print(max_result)
print(min_result)
