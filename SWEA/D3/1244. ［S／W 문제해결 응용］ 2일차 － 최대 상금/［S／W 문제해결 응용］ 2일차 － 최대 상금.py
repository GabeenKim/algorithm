def swap(cnt, chance):
    global answer 
    if cnt == chance :
        temp = ''.join(num)
        if answer < temp :
            answer = temp 
        return 
    
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            num[i], num[j] = num[j], num[i]
            temp = ''.join(num)
            if visited.get((temp, cnt),1): 	#중복이 아니라면
                visited[(temp, cnt)] = 0	#visited에 저장 
                swap(cnt+1, chance)
            num[i], num[j] = num[j], num[i]
                

T = int(input())
for i in range(1, T+1) :
    num, chance = input().split()
    chance = int(chance)
    num = list(num)
    visited = {}	#중복방지용 
    answer = '000000'	#정답 담을 변수
    
    swap(0,chance)
    
    print(f'#{i} {answer}')
        