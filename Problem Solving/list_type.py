# Find Max and Min in Array

#Approach: Ekbar loop chaliye, max ar min track kora.
def find_max_min(arr):
    if not arr:
        return None, None
    max_val = min_val = arr[0]
    print("First", max_val, min_val)
    for num in arr[1:]:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val, min_val

# Dry run: arr = [3, 7, 2, 9, 4]
# start: max=3, min=3
# 7 -> max=7
# 2 -> min=2
# 9 -> max=9
# 4 -> kono change na
# final: max=9, min=2


# print(find_max_min([3, 7, 2, 9, 4])) 
# 
# Time: O(n) — ekbar e shob element dekha lage. 
# Space: O(1) — extra kono data structure lagche na.


#Practice Problem 2: Reverse an Array

#Approach: Two-pointer technique — ekta pointer shuru theke, arekta shesh theke, dujon ke 
# swap kore majher dike agiye jete thako.

def reverse_array(arr):
    left, right = 0, (len(arr) - 1)
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Dry run: arr = [1, 2, 3, 4, 5]
# left=0, right=4 -> swap arr[0],arr[4] -> [5,2,3,4,1]
# left=1, right=3 -> swap arr[1],arr[3] -> [5,4,3,2,1]
# left=2, right=2 -> loop stop (left < right fail)
# print(reverse_array([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]
# Time: O(n) — half element porjonto ghure kintu tao O(n) e count hoy. 
# Space: O(1) — in-place kora hoyeche (notun array lages nai).



# Practice Problem 3: Find Duplicates in Array
# Approach: Ekta set use kore already dekha element track kora.

def find_duplicate(arr):
    seen = set()
    duplicate = set()
    for num in arr:
        if num in seen:
            duplicate.add(num)
        else:
            seen.add(num)
    return list(duplicate)

# Dry run: arr = [1, 2, 3, 2, 4, 1]
# 1 -> seen={1}
# 2 -> seen={1,2}
# 3 -> seen={1,2,3}
# 2 -> already in seen -> duplicates={2}
# 4 -> seen={1,2,3,4}
# 1 -> already in seen -> duplicates={2,1}
# print(find_duplicate([1, 2, 3, 2, 4, 1, 4])) # [1, 2] (order vary korte pare, set unordered)


# Practice Problem 4: Rotate Array (by k positions)
# Approach: Slicing use kore array ke 2 ta part e vag kore reorder kora.

def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k] if k != 0 else arr


# Dry run: arr = [1,2,3,4,5,6,7], k=3
# k%7 = 3
# arr[-3:] = [5,6,7]
# arr[:-3] = [1,2,3,4]
# result = [5,6,7,1,2,3,4]
print(rotate_array([1, 2, 3, 4, 5, 6, 7], 4)) # [5, 6, 7, 1, 2, 3, 4]