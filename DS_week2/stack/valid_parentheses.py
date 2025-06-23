def isValid(s):
    stack = []
    pair = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in pair.values():
            stack.append(char)
        elif char in pair:
            if not stack or stack.pop() != pair[char]:
                return False
    return not stack

# Test

print(isValid("()[]{}"))  # True
print(isValid("([)]"))    # False
