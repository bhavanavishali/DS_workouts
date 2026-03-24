from collections import deque

class Mystack:
    def __init__(self):
        self.q1=deque()
        self.q2=deque()
        
    def push(self,x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1,self.q2=self.q2,self.q1
        
    def pop(self):
        return self.q1.popleft()
    def display(self)
    def top(self):
        return self.q1[0]
    
    
s=Mystack() 
s.push(10) 
s.push(20)
s.push(30)
s.push(40)
s.push(50)


print("pop element",s.pop())
print("pop element",s.pop())
print("top element",s.top())