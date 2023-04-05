# 총 일수를 더하고 7로 나머지 구한 뒤 요일 찾기 
x,y = map(int,input().split())

day=['SUN','MON','TUE','WED','THU','FRI','SAT']
last_day = [31,28,31,30,31,30,31,31,30,31,30,31]
num =0 

for i in range(0,x-1):
    num += last_day[i] 

num = (num + y)%7
print(day[num])