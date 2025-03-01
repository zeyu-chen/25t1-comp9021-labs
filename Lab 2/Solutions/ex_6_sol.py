def f6_1(n: int) -> None:
    """
    Decompose an integer n into the form 2^k * m where m is odd (or 0).
    
    This is a straightforward iterative implementation that repeatedly
    divides by 2 and counts how many times the division is possible.
    
    Time complexity: O(log n) - we divide by 2 until reaching an odd number
    Space complexity: O(1) - uses only a constant amount of extra space
    
    Args:
        n: The integer to decompose
    """
    if not n:
        print('0 = 2^k * 0 for all integers k!')
        return
    k = 0
    m = n
    sign = '-' if n < 0 else ''
    while m % 2 == 0:
        m //= 2        # Integer division by 2
        k += 1         # Increment power counter
    print(f'{n} = {sign}2^{k} * {abs(m)}')


def f6_2(n: int) -> None:
    """
    Decompose an integer n into the form 2^k * m using bit manipulation.
    
    This approach uses bitwise operations to directly count trailing zeros,
    which can be more efficient for large numbers as it works at the bit level.
    
    Time complexity: O(log n) - in worst case, checks each bit position
    Space complexity: O(1) - uses only a constant amount of extra space
    
    Args:
        n: The integer to decompose
    """
    if n == 0:
        print('0 = 2^k * 0 for all integers k!')
        return
    
    # Get absolute value and sign
    abs_n = abs(n)
    sign = '-' if n < 0 else ''
    
    # Count trailing zeros using bit manipulation
    if abs_n:
        k = 0
        while (abs_n & 1) == 0:  # Check if least significant bit is 0
            abs_n >>= 1  # Right shift by 1 (equivalent to division by 2)
            k += 1
    
    print(f'{n} = {sign}2^{k} * {abs_n}')


def f6_3(n: int) -> None:
    """
    Decompose an integer n into the form 2^k * m using binary representation.
    
    This approach leverages the binary string representation to count trailing
    zeros directly. It offers a more conceptual approach that demonstrates how
    the problem relates to binary representation.
    
    Time complexity: O(log n) - converting to binary and checking digits
    Space complexity: O(log n) - for storing the binary representation
    
    Args:
        n: The integer to decompose
    """
    if n == 0:
        print('0 = 2^k * 0 for all integers k!')
        return
    
    abs_n = abs(n)
    sign = '-' if n < 0 else ''
    
    # Convert to binary and strip trailing zeros
    bin_repr = bin(abs_n)[2:]  # Remove '0b' prefix
    k = len(bin_repr) - len(bin_repr.rstrip('0'))
    
    # Calculate m by integer division
    m = abs_n // (2 ** k)
    
    print(f'{n} = {sign}2^{k} * {m}')


def f6_4(n: int) -> None:
    """
    Decompose an integer n into the form 2^k * m using recursion.
    
    This approach demonstrates a recursive solution where each recursive call
    divides the number by 2 and increments k. It uses a nested function to 
    maintain the original input value throughout the recursion.
    
    Time complexity: O(log n) - we make log(n) recursive calls at most
    Space complexity: O(log n) - for the recursion call stack
    
    Args:
        n: The integer to decompose
    """
    if n == 0:
        print('0 = 2^k * 0 for all integers k!')
        return
    
    original_n = n
    sign = '-' if n < 0 else ''
    
    def decompose(num, k=0):
        abs_num = abs(num)
        if abs_num % 2 != 0:
            print(f'{original_n} = {sign}2^{k} * {abs_num}')
            return
        decompose(num // 2, k + 1)
    
    decompose(n)