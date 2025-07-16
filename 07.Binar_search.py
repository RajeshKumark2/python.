def binar_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target: 
            low = mid + 1  
        else:
            high < mid - 1
    return
arr = [2, 5, 8, 12, 16]
print(binar_search(arr, 12)) 
 