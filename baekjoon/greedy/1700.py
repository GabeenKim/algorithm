n, k = map(int, input().split())
order = list(map(int, input().split()))

hole = []
ans = 0

for i in range(k):
    #멀티탭에 해당 기기가 이미 있는 경우
    if order[i] in hole: continue

    #멀티탭에 유효공간이 있는 경우
    if len(hole) < n:
        hole.append(order[i])

    else:
        #val : 가장 나중에 사용될 기기, idx = 인덱스 비교를 위한 변수, tmp : 현재 기기 이후로 사용될 기기들
        val = 0
        idx = -1
        tmp = order[i:]
        #멀티탭에 자리도 없고 현재 기기가 원래 꽂혀 있지도 않으니 빼야함
        ans += 1

        for j in hole:
            #가장 나중에 사용되는 기기의 인덱스
            if j in tmp:
                target = tmp.index(j)
                if idx < target:
                    idx = target
                    val = j
            #더 이상 사용되지 않는 기기
            else:
                val = j
                break
        hole.remove(val)
        hole.append(order[i])

print(ans)
