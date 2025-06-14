def fact(n):
    if n==1:
        return 1
    
    return n*fact(n-1)
print(fact(5))



#workflow


# factorial(5)
# = 5 * factorial(4)
# = 5 * (4 * factorial(3))
# = 5 * (4 * (3 * factorial(2)))
# = 5 * (4 * (3 * (2 * factorial(1))))
# = 5 * 4 * 3 * 2 * 1
# = 120
