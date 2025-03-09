def f6_1(L: list[list[int]], fields: list[int]) -> list[list[int]]:
    """
    Sorts a list of lists of integers based on specified fields priority.
    
    Uses Python's built-in sorted function with a custom key function that creates
    a tuple of values in the order specified by fields.
    
    Args:
        L: A list of lists of integers, all inner lists have the same length
        fields: A list representing a permutation of {1, ..., n}, where n is the length
               of each inner list, determining sort priority
    
    Returns:
        A new sorted list of lists of integers
    """
    # Use sorted with a custom key function
    # - The lambda creates a tuple of values for each inner list
    # - For each position i in fields, we get the corresponding value from the inner list (x[i-1])
    # - The tuple is then used for comparison, checking elements in the order specified by fields
    return sorted(L, key=lambda x: tuple(x[i - 1] for i in fields))


def f6_2(L: list[list[int]], fields: list[int]) -> list[list[int]]:
    """
    Sorts a list of lists of integers based on specified fields priority.
    
    Uses operator.itemgetter for more efficient access to list elements.
    
    Args:
        L: A list of lists of integers, all inner lists have the same length
        fields: A list representing a permutation of {1, ..., n}
    
    Returns:
        A new sorted list of lists of integers
    """
    from operator import itemgetter
    
    # Create a copy of L to avoid modifying the original list
    result = L.copy()
    
    # Sort in reverse order of fields (least significant to most significant)
    # This creates a stable sort where earlier sorts are preserved for ties
    for field in reversed(fields):
        # Adjust index (fields are 1-indexed, Python is 0-indexed)
        index = field - 1
        # Sort the list based on the current field
        result.sort(key=itemgetter(index))
    
    return result


def f6_3(L: list[list[int]], fields: list[int]) -> list[list[int]]:
    """
    Sorts a list of lists of integers based on specified fields priority.
    
    Uses a custom comparison function with functools.cmp_to_key.
    
    Args:
        L: A list of lists of integers, all inner lists have the same length
        fields: A list representing a permutation of {1, ..., n}
    
    Returns:
        A new sorted list of lists of integers
    """
    from functools import cmp_to_key
    
    # Define a comparison function that compares two lists based on fields
    def compare_lists(list1: list[int], list2: list[int]) -> int:
        for field in fields:
            index = field - 1  # Convert to 0-indexed
            # Compare elements at the current field
            if list1[index] < list2[index]:
                return -1
            elif list1[index] > list2[index]:
                return 1
        # If all fields are equal
        return 0
    
    # Use the comparison function with sorted
    return sorted(L, key=cmp_to_key(compare_lists))


def f6_4(L: list[list[int]], fields: list[int]) -> list[list[int]]:
    """
    Sorts a list of lists of integers based on specified fields priority.
    
    Implements merge sort algorithm with custom comparison.
    
    Args:
        L: A list of lists of integers, all inner lists have the same length
        fields: A list representing a permutation of {1, ..., n}
    
    Returns:
        A new sorted list of lists of integers
    """
    # Make a copy to avoid modifying the original list
    result = L.copy()
    
    # Define a function to compare two lists based on fields
    def is_less_than(list1: list[int], list2: list[int]) -> bool:
        for field in fields:
            index = field - 1  # Convert to 0-indexed
            if list1[index] < list2[index]:
                return True
            elif list1[index] > list2[index]:
                return False
        # If all fields are equal
        return False
    
    # Implement merge sort
    def merge_sort(arr: list[list[int]]) -> list[list[int]]:
        if len(arr) <= 1:
            return arr
            
        # Divide the array
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        # Merge the sorted halves
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if is_less_than(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        # Add remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    # Apply merge sort and return the result
    return merge_sort(result)

