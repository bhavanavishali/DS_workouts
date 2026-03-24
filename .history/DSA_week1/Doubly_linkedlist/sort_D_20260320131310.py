        
def sort_d(self):
        temp1=self.head
        while temp1:
            temp2=temp1.next
            while temp2:
                if temp1.data > temp2.data:
                    temp1.data,temp2.data =temp2.data,temp1.data
                temp2=temp2.next
            temp1=temp1.next