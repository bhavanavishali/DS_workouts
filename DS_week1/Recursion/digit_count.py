def num_digit(n):

    if len(str(n))==1:
        return 1
    
    return 1+num_digit(n//10)

print(num_digit(12365))