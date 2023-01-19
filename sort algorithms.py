##### Sort Algorithms #####
""" 
This file contain almost all sorting algorithms that are usually widely used.

1- Bubble sort algorithm
2- Insertion sort algorithm
3- Shell sort algorithm
4- Selection sort algorithm
5- Counting sort algorithm
6- Quick sort algorithm
7- Merge sort algorithm
8- Heap sort algorithm

- Every algorithm has been implemented to sort a simple python list (or array).
- Including time and space complexity for each one.
-  //  //  docs & comments to get better understanding.
"""

def bubbleSort(arr: list) -> list:
    """ ==> bubble sort algorithm <==
    - compare each element with its next one and swap if necessary.
    - time complexity = O(n^2)
    - space complexity = O(1) """

    # looping through arr items except arr[-1] to avoid indexing error
    for _ in range(len(arr)-1):
        stop = False # stop iteration when the rest are sorted
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]: # simple comparision
                arr[i], arr[i+1] = arr[i+1], arr[i] # swap the 2 values if condition is True
                stop = True
        if not stop:
            return arr
    return arr    


def insertionSort(arr: list) -> list:
    """ ==> insertion sort <==
    - take an anchor in which all i on its right are sorted, compare it with the left side.
    - time complexity = O(n^2)
    - space complexity = O(1) """

    # looping through arr items from arr[1]
    for i in range(1, len(arr)):
        anchor = arr[i] # to make all i before it sorted
        j = i - 1
        while j >= 0 and anchor < arr[j]:
            arr[j+1] = arr[j] # swap the 2 values if condition is True
            j -= 1
        arr[j+1] = anchor # changing the anchor = all i before it are sorted
    return arr


def shellSort(arr: list) -> list:
    """ ==> shell sort algorithm <==
    - inhance the insertion sort, reduce the comparision times as possible.
    - time complexity = O(n(log(n))^2)
    - space complexity = O(1) """

    gap = len(arr) // 2 # when gap = 1 we are with the insertion sort
    while gap > 0:
        for i in range(gap, len(arr)): # from gap not 0 to cover all arr items with the same gap, because of j-gap
            anchor, j = arr[i], i # almost the same as insertion sort
            while j >= gap and anchor < arr[j-gap]: # dealing only with sub_arr not all i
                arr[j-gap], arr[j] = arr[j], arr[j-gap] # swap the 2 values if condition is True
                j -= gap # to keep movig with i
        gap //= 2
    return arr


def selectionSort(arr: list) -> list:
    """ ==> shell sort algorithm <==
    - take the min and compare it with the 1st of the left arr and so on (similar to insertion sort).
    - time complexity = O(n^2)
    - space complexity = O(1) """

    # looping through arr items except arr[-1] to avoid indexing error
    for i in range(len(arr)-1):
        min_index = i # initialize the minimum index
        for j in range(i+1, len(arr)): # from 0 -> i should be sorted
            if arr[min_index] > arr[j]:
                min_index = j # updating the min_index if condition is True
        if min_index > i: 
            arr[min_index], arr[i] = arr[i], arr[min_index] # swap the 2 values if condition is True
    return arr


def countingSort(arr: list) -> list:
    """ ==> counting sort algorithm <==
    - based on the range of arr values and the count of each element.
    - time complexity = O(n+k)
    - space complexity = O(k) """

    arr_size = len(arr)
    max_arr = arr[0] # find the max of arr to create the counting arr with size of max_arr+1
    for i in range(len(arr)-1): # we could use max() built-in func
        for j in range(i+1, arr_size):
            if max_arr < arr[j]:
                max_arr = arr[j]
    count_arr = [0] * (max_arr+1) # initialize the count_arr with size= max_arr+1
    for each in range(arr_size):
        count_arr[arr[each]] += 1 # counting the occurrence of every i in arr
    for each in range(1, len(count_arr)):
        count_arr[each] += count_arr[each-1] # counting the cumulative sum of items in count_arr
    
    # new pos of every i in arr = value of count_arr[i] - 1
    result = [0] * arr_size
    for index in range(arr_size):
        result[count_arr[arr[index]]-1] = arr[index]
        count_arr[arr[index]] -= 1 # in case we found repetitive value
    for item in range(arr_size): # we could use arr = result.copy()
        arr[item] = result[item]
    return arr


def quickSort(arr: list) -> list:
    """ ==> quick sort algorithm <==
    - fix a pivot in which all i in the right side are < pivot, left > pivot, make recursive
    - time complexity(average case) = O(nlog(n))
    - time complexity(worst case) = O(n^2)
    - space complexity = O(1) """

    if len(arr) <= 1: # the base condition to terminate the recursion
        return arr
    pivot, i = arr[-1], 0 # pivot could be any value (do some research about that)
    pivot_ndx = arr.index(pivot)
    while i < pivot_ndx: # trying to make all i before pivot < & all after >
        while pivot < arr[i]:
            pivot_ndx = arr.index(pivot) # updating pivot_index if codition is True
            arr[i], arr[pivot_ndx], arr[pivot_ndx-1] = arr[pivot_ndx-1], arr[i], pivot # make necessary swaps
        i += 1
    # fix the pivot position then recursively do the same for the left & right sides
    return quickSort(arr[:arr.index(pivot)])+[pivot]+quickSort(arr[arr.index(pivot)+1:])

    # Other solution:
    # pivot = arr[-1]
    # for i in range(len(arr)-2, -1, -1):
    #     if pivot <= arr[i]:
    #         item = arr[i]
    #         arr.remove(arr[i])
    #         arr.insert(arr.index(pivot)+1, item)
    # return quickSort(arr[:arr.index(pivot)])+[pivot]+quickSort(arr[arr.index(pivot)+1:])


def mergeSort(original: list) -> list:
    """ ==> merge sort algorithm <==
    - comparing 2 sorted lists recursively, with divide & conquer concept
    - time complexity = O(nlog(n))
    - space complexity = O(n) """

    if len(original) <= 1: # the base condition to terminate the recursion
        return original

    # helper-inner func to sort and merge to sorted lists(arrays)
    def mergeSortHelper(arr1: list, arr2: list, original: list) -> list:
        i = j = k = 0
        # i for arr1(left) & j for arr2(right)
        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                original[k] = arr2[j] # updating original arr if condition is True
                j += 1
            else:
                original[k] = arr1[i] # updating original arr if condition is True
                i += 1
            k += 1
        # if still some items didn't include in the original arr...
        # ...we do so, keep in mind that these 2 sub_arr are sorted
        while i < len(arr1):
            original[k] = arr1[i] # updating original arr if condition is True
            i += 1
            k += 1
        while j < len(arr2):
            original[k] = arr2[j] # updating original arr if condition is True
            j += 1
            k += 1
        return original

    # split the original arr to 2 sub_arr until we reach len 1 for both sub_arr recursively...
    # ...using the middle of the original arr
    arr1 = original[:len(original)//2]
    arr2 = original[len(original)//2:]
    if len(arr1) == 1 and len(arr2) == 1:
        return mergeSortHelper(arr1, arr2, original) # call the helper if len is 1 for both sub_arr
    return mergeSortHelper(mergeSort(arr1), mergeSort(arr2), original) # else continue dividing then conquer


def heapSort(arr: list) -> list:
    pass


