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
# print(bubble_sort([5, 1, 4, 2, 8])) # [1, 2, 4, 5, 8]


# Selection Sort
# Idea: Protibar unsorted part theke shobcheye choto element khuje ber kore, shuru te bosiye deya.

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Dry run: arr=[29, 10, 14, 37, 13]
# i=0: min in [29,10,14,37,13] is 10 at idx1 -> swap -> [10,29,14,37,13]
# i=1: min in [29,14,37,13] is 13 at idx4 -> swap -> [10,13,14,37,29]
# i=2: min in [14,37,29] is 14 (already there)
# i=3: min in [37,29] is 29 at idx4 -> swap -> [10,13,14,29,37]
# print(selection_sort([29, 10, 14, 37, 13])) # [10, 13, 14, 29, 37]


# Time: O(n^2) — always, best case-o. Space: O(1). Kokhon use korbo: Jokhon swap-er cost beshi hote pare kintu swap-er
# shonkha kom rakhte chao (selection sort e maximum n-1 bar swap hoy).


# Insertion Sort
# Idea: Card khela shajanor moto — protiti notun element take already-sorted part-er sathik jaygay "insert" kora.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    
    return arr


# Dry run: arr=[12, 11, 13, 5, 6]
# i=1: key=11, shift 12 -> [11,12,13,5,6]
# i=2: key=13, no shift needed -> [11,12,13,5,6]
# i=3: key=5, shift 13,12,11 -> [5,11,12,13,6]
# i=4: key=6, shift 13,12,11 -> [5,6,11,12,13]
print(insertion_sort([12, 11, 13, 5, 6])) # [5, 6, 11, 12, 13]