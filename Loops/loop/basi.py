# fruits = ['apple', 'banana', 'cherry']
# for furit in fruits:
#     print(furit)



# for num in range(10): 
#     if num == 3:
#         continue
#     if num == 8:
#         break
#     print(num)
    

def firt_duplication(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return - 1
print(firt_duplication([3, 2, 1, 2, 4]))


