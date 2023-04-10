def factorial_iteractive(n) :
    if n <= 1:
        return 1
    return n*(factorial_iteractive(n-1))

print(factorial_iteractive(5))