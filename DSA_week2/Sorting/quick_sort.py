def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot=arr[0]
    left=[x for x in arr[1:] if x <=pivot]
    right=[x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

arr=[4,6,8,3,8]
print("original aray",arr)
arr=quick_sort(arr)
print("sorted ",arr)


