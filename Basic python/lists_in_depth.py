# arr = [10, 20, 30, 40, 50]

# print(arr[0])
# print(arr[-1])


# Method 1: index diye

# for i in range(len(arr)):
#     print(arr[i])

# Method 2: direct value diye
# for val in arr:
#     print(val)


# Method 3: index + value dujon e lagle
# for i, val, in enumerate(arr):
#     print(i, "->", val)

#################Insertion#########################
arr = [10, 20, 30, 40, 50]
# arr.append(45)
# arr.insert(2, 55)

# print(arr)



#################Deletion#########################
# arr.pop()
# arr.pop(1)
# arr.remove(20)




#################Searching#########################



print(30 in arr)
print(arr.index(50))