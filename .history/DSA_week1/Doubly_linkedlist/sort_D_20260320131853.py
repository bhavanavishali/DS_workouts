def sort_d(self):
        temp1=self.head
        while temp1:
            temp2=temp1.next
            while temp2:
                if temp1.data > temp2.data:
                    temp1.data,temp2.data =temp2.data,temp1.data
                temp2=temp2.next
            temp1=temp1.next


def middle(self):
        fast=self.head
        slow=self.head
        
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        if slow:
            print(f"{slow.data}")