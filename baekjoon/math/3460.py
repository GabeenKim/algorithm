t = int(input())

for _ in range(t) :
    bi_n = bin(int(input()))[2:]
    for i in range(len(bi_n)) :
        if bi_n[-i-1] == '1' :
            print(i, end= " ")  
    