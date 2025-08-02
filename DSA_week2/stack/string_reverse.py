def string_rev(s):
    stack=[]
    for char in s:
        stack.append(char)
    rev=""
    while stack:
        rev+=stack.pop()
        
    return rev
    
print(string_rev("hello"))
