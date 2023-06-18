def solution(name, yearning, photo):
    answer = []
    
    for i in range(len(photo)) :
        sum_num = 0
        for j in photo[i]:
            if j in name:
                idx = name.index(j)
                sum_num += yearning[idx]
            else : sum_num += 0 
        answer.append(sum_num)
    return answer