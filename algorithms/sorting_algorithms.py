# Bubble Sort
# Idea: Baar baar ashe pashe-r duita element compare kore, boro ta ke pichone "bubble up" kore pathiye deya.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr



# Dry run: arr=[5,1,4,2,8]
# Pass 1: compare(5,1)->swap->[1,5,4,2,8]; compare(5,4)->swap->[1,4,5,2,8];
# compare(5,2)->swap->[1,4,2,5,8]; compare(5,8)-> no swap
# Pass 2: [1,2,4,5,8] mostly sorted...
print(bubble_sort([5, 1, 4, 2, 8])) # [1, 2, 4, 5, 8]