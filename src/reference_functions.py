#def binary_sort (arr):

def binary_search_sorted_array (arr, findMe):
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

