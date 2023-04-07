s = input()

number = 0
alpha = []

for data in s :
  #알파벳인 경우 리스트에 삽입
  if data.isalpha():
    alpha.append(data)
  #숫자는 따로 더함
  else :
    number += int(data)
 
alpha.sort()

#숫자가 하나라도 있으면 알파벳 가장 뒤에 삽입
if number != 0 :
  alpha.append(str(number))

#리스트를 문자열로 변환하여 출력
print(''.join(alpha))