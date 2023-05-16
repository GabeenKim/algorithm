t = int(input())
num = ['0001101','0011001','0010011','0111101','0100011','0110001','0101111','0111011','0110111','0001011']

for tc in range(1,t+1):
    n, m = map(int,input().split())
    arr =[]
    code = []
    start = m-1
    for i in range(n):
        string = input()
        if len(string.strip('0')) != 0 :
            arr.append(string)

    for i in arr:
        for j in range(m-1,-1,-1):
            if i[j] == '1':
                start = j
                break
            start -= 1
        for _ in range(m//7):
            if i[start-6:start+1] in num :
                code.append(num.index(i[start-6:start+1]))
                start -= 7

    code.reverse()
    code = [code[i*8:i*8+8] for i in range(len(code)//8)]

    odd, even = 0,0
    for i in range(4):
        odd += code[0][i*2]
        even += code[0][i*2+1]
    if ((odd*3) + even) % 10 == 0:
        print(f'#{tc} {odd+even}')
        continue
    print(f'#{tc} 0')

