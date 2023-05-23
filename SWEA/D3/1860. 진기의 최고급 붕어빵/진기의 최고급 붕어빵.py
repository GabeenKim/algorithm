t = int(input())
for tc in range(1,t+1):
    n, m, k = map(int, input().split())
    customer = list(map(int, input().split()))
    customer.sort()

    pos = True
    for i in range(n) :
        made = (customer[i]//m)*k - (i+1)
        if made < 0 :
            pos = False
            break

    if pos :
        print(f'#{tc} Possible')
    else :
        print(f'#{tc} Impossible')
