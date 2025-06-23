def binaryserch(arr,target,left=0,right=None):
    if right is  None:
        right=len(arr)-1
    if left >right:
        return -1
    while left <=right:
        mid=(right+left)//2
        
        if arr[mid]==target:
            return mid
            
        elif target >  arr[mid]:
            left=mid+1
        else:
     
            right=mid-1
    return -1
    
arr=[5,10,15,20,55]
print(binaryserch(arr,55))