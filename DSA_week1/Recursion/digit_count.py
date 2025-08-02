def num_digit(n):

    if n==0:
        return 0
    
    return 1+num_digit(n//10)

print(num_digit(12365))