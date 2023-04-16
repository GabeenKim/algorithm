n ,m = map(int,input().split())
arr_n = []

for i in range(n):
    arr_n.append(int(input()))

#INF 값으로 초기화
d = [10001] * (m+1)

#보텀업으로 DP 
d[0] = 0

for i in range(n):  #i : 화폐단위
    for j in range(arr_n[i], m +1):   # j : 금액
        if d[j-arr_n[i]] != 10001:  #(i-k)번째에 값이 존재하는 경우 
            d[j] = min(d[j], d[j-arr_n[i]]+1)

if d[m] == 10001 : print(-1)
else : print(d[m])