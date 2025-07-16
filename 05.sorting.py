def sorting(arr):
    if len(arr) <= 1:
        return arr 
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return sorting(left) + middle + sorting(right)
print(sorting([6, 3, 1, 2])) 