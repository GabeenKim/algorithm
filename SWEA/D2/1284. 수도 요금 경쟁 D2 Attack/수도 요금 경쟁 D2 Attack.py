t = int(input())
for tc in range(1, t+1):
    p, q, r, s,w = map(int, input().split())
    a_price, b_price= p * w, q
    ans = 0
    if w > r :
        b_price = q + (w-r)*s
        if a_price < b_price : ans = a_price
        else : ans = b_price
    else :
        if a_price < b_price:
            ans = a_price
        else:
            ans = b_price
    print(f'#{tc} {ans}')