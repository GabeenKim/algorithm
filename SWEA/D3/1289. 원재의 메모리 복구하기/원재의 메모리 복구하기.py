t = int(input())

for tc in range(1,t+1):
    memory = input()
    cur = ['0'] * len(memory)
    ans = 0
    for i in range(len(memory)):
        if memory[i] != cur[i]:
            ans += 1
            for k in range(i, len(memory)):
                cur[k] = memory[i]
            
    print(f'#{tc} {ans}')