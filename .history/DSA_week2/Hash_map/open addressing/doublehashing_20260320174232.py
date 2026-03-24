class DoubleHash:

    def __init__(self,size):
        self.size=size
        self.items=[None]*self.size
        self.count=0
        
    def myhash(self,key):
        return key % self.size
        
    def myhash1(self,key):
        return 7 - (key % 7)

        
    def insert(self,key):

        index=self.myhash(key)

        i=0
        while i < self.size and self.items[(index+i*self.myhash1(key))%self.size] is not None:
            i+=1
            
        new_index=(index+i*self.myhash1(key))%self.size
        self.items[new_index]=key
        self.count+=1
        
        if self.count/self.size >0.7:
            self.rehashing()
            
            
    def rehashing(self):
        
        old_items=self.items
        
        self.size=self.size*2
        self.items=[None]*self.size
        self.count=0
        
        for item in old_items:
            if item is not None:
                self.insert(item)


    def display(self):
        print(self.items)


lb=DoubleHash(10)

a=[10,5,61,40]

for i in a:
    lb.insert(i)

lb.display()