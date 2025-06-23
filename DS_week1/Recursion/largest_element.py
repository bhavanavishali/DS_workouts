def largest_num(arr):
    if len(arr)==1:
        return arr[0]
    
    maxi=largest_num(arr[1:])

    if arr[0] > maxi:
        return arr[0]
    else:
        return maxi

   
arr=[5,6,3]
print(largest_num(arr))

