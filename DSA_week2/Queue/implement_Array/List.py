class Queue:

    def __init__(self):
        self.queue=[]

    def enqueue(self,x):
        self.queue.append(x)
    
    def dequeue(self):
        if not self.queue:
            return "queue empty"
        self.queue.pop(0)
    def peek(self):
        if not self.queue:
            return "Queue empty"
        self.queue[0]

    def display(self):
        print("Queue",self.queue)

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
x=q.dequeue()

print("delete",x)
x=q.dequeue()
print("delete",x)
q.display()

