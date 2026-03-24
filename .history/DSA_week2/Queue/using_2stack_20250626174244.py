class Queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    
    def enqueue(self,x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2 :
            while self.stack1:

                self.stack2.append(self.stack1.pop())
            if self.stack2 is None:
                return "stack is empty"
            return self.stack2.pop()
        
q=Queue()
q.enqueue(100)
q.enqueue(200)
q.enqueue(300)
print("delete element",q.dequeue())


