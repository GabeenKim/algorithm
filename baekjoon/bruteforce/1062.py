#비트마스킹 활용하기
from itertools import combinations
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
#antic 중 하나라도 모르면 어떤 단어도 배울 수 없으므로 0출력 후 종료
if k < 5:
    print(0)
    sys.exit()

#알파벳 전부를 알면 모든 단어를 배울 수 있으므로 n개 출력 후 종료
elif k == 26:
    print(n)
    sys.exit()

#읽을 수 있는 단어의 최댓값
ans = 0 
#word 배열에 n개의 단어의 각 문자의 비트 마스킹을 저장한다. 
word = []
for _ in range(n):
    s = 0
    for i in list(input().rstrip()):
        s |= (1<<(ord(i)-ord('a')))
    word.append(s)

#else_alpha : 필수 글자를 제외한 알파벳, need : a,n,t,i,c 필수 알파벳
else_alpha = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']
need = ['a','c','i','n','t']

for j in combinations(else_alpha,k-5) :
    each = 0
    res = 0
    #필수 알파벳 조합에 대한 비트마스킹
    for i in need :
        each |= 1<<(ord(i)-ord('a'))
    #나머지 알파벳 조합에 대한 비트마스킹
    for i in j:
        each |= 1<<(ord(i)-ord('a'))

    #입력받은 단어와 각 조합 비교
    for i in word:
        #i번째 알파벳이 각 조합에 포함되어 있다면 읽을 수 있는 단어 +1
        if each & i == i :
            res += 1
    #최댓값 갱신
    if ans < res : 
        ans = res

print(ans)