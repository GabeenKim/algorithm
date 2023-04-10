stack =[]

#5, 2, 3, 7 삽입-> 삭제-> 1, 4 삽입-> 삭제
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(4)

stack.pop()

stack.append(1)
stack.append(4)

stack.pop()

print(stack[::-1])