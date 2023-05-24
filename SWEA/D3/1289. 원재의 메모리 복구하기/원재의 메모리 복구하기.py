t = int(input())

for tc in range(1,t+1):
    memory = input()
    # 0번째 bit가 1이면 1111처럼 복구해야하므로 cnt +1
    if memory[0] == '0':
        ans = 0
    else : ans = 1

   # 앞과 뒤의 비트가 다를 때마다 복구작업을 해야하므로 두 자리만 비교해도 됨.
    for i in range(len(memory) -1):
        if memory[i] != memory[i+1]:
            ans+=1
    print(f'#{tc} {ans}')