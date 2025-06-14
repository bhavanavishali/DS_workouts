def descending_n(n):
    if n==0:
        return 1
    print(n)
    descending_n(n-1)
    

descending_n(10)