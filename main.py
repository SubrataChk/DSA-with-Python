# Space Complexity
# Space complexity mane hocche algorithm ta koto extra memory use kore (input bad diye). Jemon:

# def sum_all(arr):
#     total = 0
#     for i in arr:
#         total += i
#     return total

# print(sum_all([1, 2, 3, 4, 5]))

"""
Ei function a amra sudu total variable ta extra rakchi. Input size jotoi hok extra space a shomoy constant thkchja
tai ata O(1) space complexity.
"""

# def double_all(arr):
#     new_arr = []
#     for i in arr:
#         new_arr.append(i * 2)
#     return new_arr

# print(double_all([1, 2, 3, 4, 5]))

"""
Ei function a amra new_arr variable ta extra rakchi. Input size jotoi hok extra space a shomoy linear thkchja
tai ata O(n) space complexity.
"""



# Code diye Big-O bujhi
# O(1) example — constant time
def get_first_element(arr):
    return arr[0]

print(get_first_element([1, 2, 3, 4, 5]))

# O(n) example — linear time
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

print(find_max([1, 4, 5, 6, 4, 3, 2, 22]))

# O(n^2) example — quadratic time
def has_duplicate_bruteforce(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    return False

print(has_duplicate_bruteforce([1,2,3,4,5,6,7,8,9, 1]))