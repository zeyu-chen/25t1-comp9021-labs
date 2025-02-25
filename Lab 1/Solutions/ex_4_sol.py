def f4_1(D: dict[int, int], n: int) -> list[int]:
    """
    Uses a while loop to iteratively build the sequence.
    This is a simple and direct non-recursive implementation.
    """
    if n not in D:
        return []
    
    L = [n]
    while n in D and n < D[n]:
        n = D[n]
        L.append(n)
    
    return L


def f4_2(D: dict[int, int], n: int) -> list[int]:
    """
    Uses recursion to build the sequence.
    Base case is when n is not in D.
    Always includes D[n] if n is in D.
    """
    if n not in D:
        return []
    
    next_val = D[n]
    if n < next_val:
        rest_of_sequence = f4_2(D, next_val) if next_val in D else []
        return [n] + ([next_val] if next_val not in D else []) + rest_of_sequence
    else:
        return [n]


def f4_3(D: dict[int, int], n: int) -> list[int]:
    """
    Uses a set to detect and avoid cycles.
    Prevents infinite loops in more complex dictionary structures. Safer than f4_1.
    """
    if n not in D:
        return []
    
    result = [n]
    current = n
    visited = {n}
    
    while current in D:
        next_val = D[current]
        if current < next_val and next_val not in visited:
            result.append(next_val)
            current = next_val
            visited.add(current)
        else:
            break
    
    return result


def f4_4(D: dict[int, int], n: int) -> list[int]:
    """
    Uses the dictionary's get method to simplify condition checking.
    Uses default values to avoid KeyError exceptions.
    """
    if n not in D:
        return []
    
    result = [n]
    current = n
    
    while True:
        next_val = D.get(current, current)  # Returns current value if key doesn't exist
        if current < next_val:
            result.append(next_val)
            current = next_val
        else:
            break
    
    return result