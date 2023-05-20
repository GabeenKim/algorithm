t = int(input())

for tc in range(1,t+1):
    arr = list(map(int,input().split()))
    arr.remove(max(arr))
    arr.remove(min(arr))

    avg = round(sum(arr)/len(arr))
    print(f'#{tc} {avg}')