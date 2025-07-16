def marge(left, right):
    result = []
    i = j = 0 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1 
        else:
             result.appedn(right[j])
             j += 1 
        result.extend(left[i:] or right[j:])
        return result 
    
    def merg_sort(arr):
        if len(arr) <= 1:
            return arr 
        mid = len(arr)//2
        left = merg_sort(arr[:mid])
        right = merg_sort(arr[mid:])
        return marge(left, right)
    
    
