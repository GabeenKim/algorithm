t = int(input())

grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1,t+1):
    n, k = map(int,input().split())
    std = [list(map(int,input().split())) for _ in range(n)]

    score = []
    for i in std:
        score.append(i[0]*0.35 + i[1]*0.45 + i[2]*0.2)
    score.sort(reverse=True)

    k_score = std[k-1][0]*0.35 + std[k-1][1]*0.45 + std[k-1][2]*0.2
    k_grade = grade[score.index(k_score)//(n//10)]
    
    print(f'#{tc} {k_grade}')