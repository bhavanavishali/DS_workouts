
def stack_palindrome(s):
    stack=list(s)
    for char in s:
        if char != stack.pop():
            return False
    return True
        
print(stack_palindrome("madassm"))
