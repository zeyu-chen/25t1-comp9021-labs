# Call special list a list whose members are integers or special lists.
# Assume that the argument L is a special list.
#
# If the returned dictionary contains a key of the form (i_1, ..., i_n),
# with as associated value the integer e, then:
# - if n == 1 then the member of L of index i_1 is e;
# - if n == 2 then the member of L of index i_1 is a
#   list L1, and the member of L1 of index i_2 is e;
# - if n == 3 then the member of L of index i_1 is a
#   list L1, and the member of L1 of index i_2 is a
#   list L2, and the member of L2 of index i_3 is e;
# ...
#
# isinstance() is useful.

from typing import Dict, List, Tuple, Any

def f5_1(L: List[Any]) -> Dict[Tuple[int, ...], int]:
    """
    Converts a special list (containing integers or other special lists) into a dictionary.

    The dictionary maps tuples of indices to integer values, where each tuple represents
    the path to an integer in the nested list structure:
    - A key (i,) maps to an integer at index i in the top-level list
    - A key (i, j) maps to an integer at index j in a sublist at index i
    - A key (i, j, k) maps to an integer at index k in a sublist at index j in a sublist at index i
    - And so on for deeper nesting levels

    This implementation uses recursion to traverse the nested list structure.

    Args:
        L: A special list containing integers or other special lists

    Returns:
        A dictionary mapping index paths (as tuples) to integer values

    Example:
        f5_1([1, [2, 3], 4]) returns {(0,): 1, (1, 0): 2, (1, 1): 3, (2,): 4}
    """
    result = {}

    # Iterate through each element in the list
    for i in range(len(L)):
        # If the element is an integer, add it to the result with its index as a tuple
        if isinstance(L[i], int):
            result[(i,)] = L[i]
        # If the element is a list, recursively process it
        else:
            # Get the dictionary for the nested list
            nested_dict = f5_1(L[i])
            # Add each entry from the nested dictionary to the result,
            # prepending the current index to each key
            for indices, value in nested_dict.items():
                result[(i,) + indices] = value

    return result


def f5_2(L: List[Any]) -> Dict[Tuple[int, ...], int]:
    """
    Converts a special list (containing integers or other special lists) into a dictionary.

    This alternative implementation uses a depth-first traversal with an explicit stack,
    but ensures the output order matches the recursive implementation by using an ordered dictionary
    and sorting the keys before returning.

    Args:
        L: A special list containing integers or other special lists

    Returns:
        A dictionary mapping index paths (as tuples) to integer values

    Example:
        f5_2([1, [2, 3], 4]) returns {(0,): 1, (1, 0): 2, (1, 1): 3, (2,): 4}
    """
    # Use a regular dictionary to collect results
    temp_result = {}

    # Initialize stack with (list, current_path) pairs
    # Each entry contains the list to process and the path to that list
    stack = [(L, ())]

    # Process items until the stack is empty
    while stack:
        current_list, path = stack.pop()

        # Iterate through the current list in reverse order (to match DFS order when using a stack)
        for i in range(len(current_list) - 1, -1, -1):
            # Calculate the full path to the current element
            current_path = path + (i,)

            # If the element is an integer, add it to the result
            if isinstance(current_list[i], int):
                temp_result[current_path] = current_list[i]
            # If the element is a list, add it to the stack for processing
            else:
                stack.append((current_list[i], current_path))

    # Create a new dictionary with keys sorted in the same order as f5_1 would produce
    # This is a lexicographical sort by the tuple elements
    result = {}
    for key in sorted(temp_result.keys()):
        result[key] = temp_result[key]

    return result