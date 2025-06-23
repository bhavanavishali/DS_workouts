def revers_stack(stack):
    temp=[]
    while stack:
        temp.append(stack.pop())
    return temp

stack=[4,5,6,3,10]
print("reverse",revers_stack(stack))


# method 2 using recursion


stack = [1, 2, 3, 4]

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
    else:
        top = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(top)

def reverse_stack(stack):
    if stack:
        top = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, top)

print("Original stack:", stack)
reverse_stack(stack)
print("Reversed stack:", stack)
