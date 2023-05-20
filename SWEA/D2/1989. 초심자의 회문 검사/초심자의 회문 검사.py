t = int(input())

for tc in range(1,t+1):
    word = input().rstrip()

    length = len(word)//2 if len(word)%2 ==0 else len(word)//2+1

    ans = 0
    for i in range(length):
        if word[i] != word[-1-i]:
            break
        else : ans = 1

    print(f'#{tc} {ans}')


