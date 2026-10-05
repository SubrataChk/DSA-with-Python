# Linear Search
# Approach: Shuru theke shesh porjonto ekta ekta kore check kora.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Dry run: arr=[4, 2, 7, 1, 9], target=7
# i=0: 4 != 7
# i=1: 2 != 7
# # i=2: 7 == 7 -> return 2
# print(linear_search([4, 2, 7, 1, 9], 7)) # 2
# print(linear_search([4, 2, 7, 1, 9], 10)) # -1

# Time: O(n) — worst case e shesh porjonto dekhte hoy. Space: O(1). 
# Kokhon use korbo: Array unsorted thakle, linear search
# e chara upay nai.




# Binary Search (Iterative)
# Approach: Array ta sorted hote hobe. 
# Middle element check kore, target choto hole left half e jao, 
# boro hole right half e jao
# — protibar search space half hoye jay.

def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low  = mid + 1
        else:
            high = mid - 1
    return -1

# Dry run: arr=[1,3,5,7,9,11,13], target=9
# low=0, high=6, mid=3 -> arr[3]=7 < 9 -> low=4
# low=4, high=6, mid=5 -> arr[5]=11 > 9 -> high=4
# low=4, high=4, mid=4 -> arr[4]=9 == 9 -> return 4
# print(binary_search_iterative([1,3,5,7,9,11,13], 9)) # 4

# Time: O(log n) — protibar search space half hoy. Space: O(1).

def binary_search_recursive(arr, target, low, heigh):
    if low > heigh:
        return True
    mid = (low + heigh) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, heigh)
    else:
        return binary_search_recursive(arr, target, low, mid - 1 )
    

arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search_recursive(arr, 5, 0, len(arr) - 1)) # 2


# Time: O(log n). Space: O(log n) — recursive call stack (iterative version e eta O(1)).
# Interview Tip: Binary search er jonno array sorted thaka must — nahole eta kaj korbe na. Interview e eta mention korte na
# bhulo.