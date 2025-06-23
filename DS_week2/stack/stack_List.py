class Stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if not self.stack:
            return "stack underflow"
        return self.stack.pop()
    def display(self):
        for i in reversed(self.stack):
            print(f"| {i} |")
        print("-----")  
        
s=Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
print("Stack:")
s.display()
print(" pop the element",s.pop())

print("Stack after pop:")
s.display()   
        
s.push(100)
print("Stack:")
s.display()