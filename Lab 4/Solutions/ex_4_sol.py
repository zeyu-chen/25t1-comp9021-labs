def f4_1(n: int) -> None:
    """
    Expresses an integer as a sum of powers of 2 (binary representation).
    
    Converts the number to binary, then interprets each '1' bit as the corresponding
    power of 2. For example, 42 (101010 in binary) is expressed as 2^5 + 2^3 + 2^1.
    Negative numbers are expressed as the negative of the powers sum.
    
    Args:
        n: An integer to express as sum of powers of 2
    """
    # Handle the special case of 0
    if not n:
        print('0 = 0')
        return
        
    # Convert number to binary representation without '0b' prefix
    binary_n = f'{n:b}'
    
    # Extract positions where binary digits are '1'
    # Reversed to process from most significant to least significant bit
    powers = (i for i in range(len(binary_n)) if binary_n[i] == '1')
    
    # Determine the operator based on sign of n
    operator = ' + ' if n >= 0 else ' - '
    
    # Print the number and equal sign (with negative sign if needed)
    print(n, '= ', end='' if n > 0 else '-')
    
    # Print the sum of powers of 2, joining with the appropriate operator
    # The power is calculated as (length of binary - position - 1)
    print(operator.join(f'2^{len(binary_n) - i - 1}' for i in powers))


def f4_2(n: int) -> None:
    """
    Expresses an integer as a sum of powers of 2 (binary representation).
    
    Uses bitwise operations to extract each power of 2 component,
    without explicitly converting to binary string.
    
    Args:
        n: An integer to express as sum of powers of 2
    """
    # Handle the special case of 0
    if n == 0:
        print('0 = 0')
        return
        
    # Store the absolute value and sign
    abs_n = abs(n)
    is_negative = n < 0
    
    # Find the powers of 2 in the number
    powers = []
    bit_position = 0
    
    # Extract each bit from the absolute value
    while abs_n > 0:
        if abs_n & 1:  # Check if the least significant bit is 1
            powers.append(bit_position)
        abs_n >>= 1    # Right shift to check next bit
        bit_position += 1
        
    # Sort in descending order to display highest power first
    powers.sort(reverse=True)
    
    # Build the expression based on sign
    terms = [f'2^{power}' for power in powers]
    
    if is_negative:
        # For negative numbers, use minus signs between terms
        operator = ' - '
        print(f'{n} = -{operator.join(terms)}')
    else:
        # For positive numbers, use plus signs between terms
        operator = ' + '
        print(f'{n} = {operator.join(terms)}')


def f4_3(n: int) -> None:
    """
    Expresses an integer as a sum of powers of 2 (binary representation).
    
    Uses a recursive approach to break down the number into powers of 2.
    
    Args:
        n: An integer to express as sum of powers of 2
    """
    # Handle the special case of 0
    if n == 0:
        print('0 = 0')
        return
        
    # Initialize variables for the output
    abs_n = abs(n)
    is_negative = n < 0
    
    # Helper function to recursively find powers of 2
    def find_powers(num, acc=None):
        if acc is None:
            acc = []
            
        if num == 0:
            return acc
            
        # Find the largest power of 2 less than or equal to num
        power = 0
        while 2 ** (power + 1) <= num:
            power += 1
            
        # Add this power to our accumulator
        acc.append(power)
        
        # Recursively process the remainder
        return find_powers(num - 2 ** power, acc)
    
    # Get the powers of 2 in descending order
    powers = find_powers(abs_n)
    
    # Build the expression based on sign
    terms = [f'2^{power}' for power in powers]
    
    if is_negative:
        # For negative numbers, use minus signs between terms
        operator = ' - '
        print(f'{n} = -{operator.join(terms)}')
    else:
        # For positive numbers, use plus signs between terms
        operator = ' + '
        print(f'{n} = {operator.join(terms)}')