t = int(input())

def is_promising(x):
    for i in range(x):
        #열이 같거나 (행 차이)=(열 차이)라면 같은 대각선 상에 있으므로 안 됨.
        if row[x] == row[i] or  abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def queen(x):
    global cnt
    # n 행까지 온거면 +1
    if x == n :
        cnt += 1
        return
    else :
        for i in range(n):
            #x행 i열에 놓을 수 있는지 확인
            row[x] = i
            if is_promising(x):
                #다음 행에 대해서도 확인
                queen(x+1)

for tc in range(1,t+1):
    n = int(input())
    #각 행에 대해서 열만 확인하면 됨. 따라서 1차원 배열만 있어도 가능.
    row = [0] * n
    cnt = 0

    queen(0)

    print(f'#{tc} {cnt}')