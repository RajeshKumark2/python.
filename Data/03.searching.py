def liner_search(items, target):
    for index, item in enumerate(items):
        if item == target:
            return index 
    return - 1
print(liner_search([2, 4, 6, 7, ], 7))    