########################################################
################# Binary Functions ####################
def binary_search (arr, findMe):
    """
    Perform a Binary search of a sorted array of values to find if a single value is in the array.

    Args:
        arr -> input array of sorted values to be searched
        FindMe -> target value to be found

    Returns:
        The index of the target value if found. Otherwise -1.

    Notes to know:
        Time Comlpexity - O(logn)
        Space Compexity - O(1) (this can vary based on other search methods used)
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        if arr[middle] == findMe:
            return middle
        
        if arr[middle] < findMe:
            left = middle + 1
        else:
            right = middle - 1

    return -1

def binary_sort(arr):
    '''
    In place sorting algorithm using binary search.

    Args:
        arr -> array to be sorted

    Returns:
        sorted array

    Notes to know:
        Time Comlpexity - O(n^2)
        Space Compexity - O(1) (this can vary based on other search methods used)
    '''
    for i in range(1, len(arr)):
        pointer = arr[i]

        left, right = 0, i
        while left < right:
            middle = (left + right) // 2
            if arr[middle] < pointer:
                left = middle + 1
            else:
                right = middle

        for j in range(i, left, -1):
            arr[j] = arr[j - 1]

        arr[left] = pointer

    return arr

########################################################
################# Merge Sort ##########################

def merge_sort(arr):
    '''
    Sort an array by merge sort method.

    Args:
        arr -> array to be sorted

    Returns:
        sorted array
        
    Notes:
        Time Complexity: O(nlogn)
        Space Complexity: O(n)
    '''
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

########################################################
################# 