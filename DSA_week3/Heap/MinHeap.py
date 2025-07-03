class Minheap:
    def __init__(self):
        self.heap=[]
    
    def parent(self,i):
        return (i-1)//2
        
    def left_child(self,i):
        return 2 * i +1
        
    def right_child(self,i):
        return 2 * i + 2
        
        
    def insert(self,key):
        self.heap.append(key)
        self._heapify_up(len(self.heap)-1)
        
    def _heapify_up(self,i):
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i],self.heap[self.parent(i)]=self.heap[self.parent(i)],self.heap[i]
            i=self.parent(i)
            
    def delete_min(self):
        if len(self.heap)==0:
            return None
            
        if len(self.heap)==1:
            return self.heap.pop()
            
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self._heapify_down(0)
        return root
        
    def _heapify_down(self,i):
        
        smallest=i
        left=self.left_child(i)
        right=self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest=left
            
        if right < len(self.heap) and self.heap[right] <self.heap[smallest]:
            smallest=right
            
        if smallest != i:
            self.heap[i],self.heap[smallest]=self.heap[smallest],self.heap[i]
            self._heapify_down(smallest)
            
    def peek(self):
        if self.heap:
            return self.heap[0]
        return None
        
    def display(self):
        print("Heap arry",self.heap)
        
        
        
heap = Minheap()

heap.insert(10)
heap.insert(4)
heap.insert(15)
heap.insert(20)
heap.insert(0)
heap.insert(9)
    
heap.display()
print(heap.peek())
print(heap.delete_min())
heap.display()