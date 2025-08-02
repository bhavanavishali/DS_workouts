def binarysearch(arr,target,right=None,left=0):

    if right is None:
        right= len(arr)-1

    if left >right:
        return -1
    
    mid=(left+right)//2

    if arr[mid]==target:
        return mid
    elif target > arr[mid] :
        
        return binarysearch(arr,target,right=right,left=mid+1,)
    else:
        
        return binarysearch(arr,target,right=mid-1,left=left)
   

arr=[4,5,6,9,90]
print(binarysearch(arr,9))

