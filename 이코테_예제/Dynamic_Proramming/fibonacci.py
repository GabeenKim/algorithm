d = [0] * 100

def fibo(x):
    # 종료 조건 
    if x ==1 or x==2 :
        return 1
    # 이미 계산한 적이 있는 문제라면 그대로 반환
    if d[x] != 0 :
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))