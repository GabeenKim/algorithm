h, w = map(int, input().split())
blocks = list(map(int, input().split()))
result = 0

for i in range(1, w - 1):  #맨 왼쪽과 오른쪽은 고일 수 없음.
    left_max = max(blocks[:i])
    right_max = max(blocks[i + 1:])

    lower_one = min(left_max, right_max)
    if blocks[i] < lower_one:  #현재가 lower_one보다 낮아야 고일 수 있음
        result += lower_one - blocks[i]

print(result)
