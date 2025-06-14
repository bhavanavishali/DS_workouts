def sum_N(n):
    if n==0:
        return 0
    return n+sum_N(n-1)

print(sum_N(5))