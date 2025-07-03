class MaxHeap:
    def __init__(self):
        self.heap = []

    
    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    # Insert a new element
    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    # Heapify up (used after insert)
    def _heapify_up(self, i):
        while i != 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # Delete and return the maximum (root)
    def delete_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    # Heapify down (used after delete)
    def _heapify_down(self, i):
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

    # Return the maximum element
    def peek(self):
        return self.heap[0] if self.heap else None

    # Display the heap array
    def display(self):
        print("Heap array:", self.heap)


heap = MaxHeap()

heap.insert(10)
heap.insert(4)
heap.insert(15)
heap.insert(20)
heap.insert(1)
heap.insert(8)

heap.display()          # Output: Heap array: [20, 15, 8, 4, 1, 10]
print(heap.peek())      # Output: 20 (max element)
print(heap.delete_max())# Output: 20
heap.display()          # Output: Updated heap after deleting max
