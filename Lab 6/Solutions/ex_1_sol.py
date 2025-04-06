# Assume that the argument L is a list of lists of integers

def f1_1(L: list[list[int]]) -> tuple[list[int], list[list[int]]]:
    """
    Flattens and sorts all elements from a list of lists, then regroups
    the sorted elements based on the original sublist lengths.

    Args:
        L: A list where each element is a list of integers.

    Returns:
        A tuple containing two lists:
        1. F: A single list with all integers from L, sorted.
        2. R: A list of lists, where sorted elements are regrouped
           according to the original lengths of sublists in L.
    """
    # Calculate the lengths of each sublist in the input list L.
    # e.g., if L = [[3, 1], [2]], lengths will be [2, 1]
    lengths = [len(L1) for L1 in L]

    # Flatten the list of lists L into a single list and sort it.
    # The list comprehension (e for L1 in L for e in L1) iterates through
    # each sublist (L1) and then each element (e) in that sublist.
    # sorted() then sorts the resulting flat list.
    # e.g., if L = [[3, 1], [2]], F will be [1, 2, 3]
    F = sorted(e for L1 in L for e in L1)

    # Reconstruct the list of lists R using the sorted elements F
    # and the original lengths.
    R = []
    # Keep track of the starting index for slicing F.
    i = 0
    # Iterate 'n' from 0 up to the number of original sublists.
    # In each iteration, 'n' corresponds to the index of the length
    # we need to use from the 'lengths' list.
    for n in range(len(L)):
        # Append a slice of F to R.
        # The slice starts at index 'i'.
        # The slice ends at index 'i + lengths[n]'.
        # The walrus operator (:=) updates 'i' in place for the next iteration.
        # It assigns the value of 'i + lengths[n]' to 'i' *after* the
        # original value of 'i' is used for the slice's end index.
        # 1st iteration (n=0): L=[[3, 1], [2]], lengths=[2, 1], F=[1, 2, 3], i=0
        #   Slice F[0 : (i := 0 + 2)] -> F[0:2] which is [1, 2]. i becomes 2. R = [[1, 2]]
        # 2nd iteration (n=1): lengths[1]=1, i=2
        #   Slice F[2 : (i := 2 + 1)] -> F[2:3] which is [3]. i becomes 3. R = [[1, 2], [3]]
        R.append(F[i : (i := i + lengths[n])])

    # Return the sorted flat list F and the reconstructed list R.
    return F, R


def f1_2(L: list[list[int]]) -> tuple[list[int], list[list[int]]]:
    """
    Flattens and sorts all elements from a list of lists, then regroups
    the sorted elements based on the original sublist lengths.

    This version uses explicit index tracking instead of the walrus operator.

    Args:
        L: A list where each element is a list of integers.

    Returns:
        A tuple containing two lists:
        1. F: A single list with all integers from L, sorted.
        2. R: A list of lists, where sorted elements are regrouped
           according to the original lengths of sublists in L.
    """
    import itertools # Moved import inside the function

    # Flatten the list of lists L into a single list F.
    # itertools.chain.from_iterable is an efficient way to flatten.
    # list() converts the iterator result into a list.
    F_flat = list(itertools.chain.from_iterable(L))

    # Sort the flattened list.
    # e.g., if L = [[3, 1], [2]], F will be [1, 2, 3]
    F = sorted(F_flat)

    # Reconstruct the list of lists R using the sorted elements F.
    R = []
    # Keep track of the current position (start index) in the sorted list F.
    current_index = 0
    # Iterate through each original sublist L1 in L to get its length.
    for L1 in L:
        # Get the length of the current original sublist.
        length = len(L1)
        # Slice the sorted list F from the current_index
        # for the required length.
        sublist = F[current_index : current_index + length]
        # Add the extracted sublist to the result R.
        R.append(sublist)
        # Update the current_index for the next iteration.
        current_index += length

    # Return the sorted flat list F and the reconstructed list R.
    return F, R
