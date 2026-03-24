def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[min] >arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]


arr=[14,5,86,79]
print("original array",arr)
selection_sort(arr)
print("after",arr)
