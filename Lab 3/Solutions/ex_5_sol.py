def f5_1(integral_part: int, fractional_part: int) -> None:
    """
    Analyzes how floating point numbers are represented with different precisions.
    
    Compares the representation of a number with its original precision and 
    with double precision, detecting trailing zeros or rounding errors.
    
    Args:
        integral_part: The integer part of the number
        fractional_part: The fractional part (as an integer)
    """
    # Determine the number of digits in the fractional part
    precision = len(str(fractional_part))
    
    # Construct the floating point number by converting parts to strings
    a_float = float(str(integral_part) + '.' + str(fractional_part))
    
    # Format with original precision
    simple_precision = f'{a_float:.{precision}f}'
    
    # Create a version with expected trailing zeros (if number is exact)
    extended_simple_precision = simple_precision + '0' * precision
    
    # Format with double precision
    double_precision = f'{a_float:.{precision * 2}f}'
    
    # Start printing the output
    print('With', precision * 2, 'digits after the decimal point, ', end='')
    
    # Compare the extended simple precision with double precision
    if extended_simple_precision == double_precision:
        # If they match, it means the number can be represented exactly with trailing zeros
        print(simple_precision, 'prints out with', precision, 'trailing',
              # Singular/plural form for "zero"/"zeroes"
              precision == 1 and 'zero,' or 'zeroes,', 'namely, as',
              extended_simple_precision
             )
    else:
        # If they don't match, it means floating point representation introduces rounding errors
        print(simple_precision, 'prints out as', double_precision)


def f5_2(integral_part: int, fractional_part: int) -> None:
    """
    Analyzes how floating point numbers are represented with different precisions.
    
    Avoids using float conversion until necessary to better control the analysis process.
    
    Args:
        integral_part: The integer part of the number
        fractional_part: The fractional part (as an integer)
    """
    # Get the length of the fractional part
    frac_len = len(str(fractional_part))
    
    # Determine the total precision needed (double the fractional digits)
    double_precision = frac_len * 2
    
    # Construct the float carefully to avoid precision issues early on
    float_str = f"{integral_part}.{fractional_part}"
    float_val = float(float_str)
    
    # Format with double precision
    formatted_double = f"{float_val:.{double_precision}f}"
    
    # Extract the actual fractional part from the formatted string for analysis
    formatted_fraction = formatted_double.split('.')[1]
    
    # Check if the second half of the fraction consists entirely of zeros
    first_half = formatted_fraction[:frac_len]
    second_half = formatted_fraction[frac_len:]
    
    # Start building the output
    print(f"With {double_precision} digits after the decimal point, ", end="")
    
    # Simple version (original precision)
    simple_version = f"{float_val:.{frac_len}f}"
    
    if second_half == '0' * frac_len:
        # No rounding errors, just trailing zeros
        print(f"{simple_version} prints out with {frac_len} trailing", 
              "zero," if frac_len == 1 else "zeroes,", 
              f"namely, as {formatted_double}")
    else:
        # Rounding errors present
        print(f"{simple_version} prints out as {formatted_double}")


def f5_3(integral_part: int, fractional_part: int) -> None:
    """
    Analyzes how floating point numbers are represented with different precisions.
    
    Uses string manipulation to avoid potential floating point inaccuracies during analysis.
    
    Args:
        integral_part: The integer part of the number
        fractional_part: The fractional part (as an integer)
    """
    # Get string representations
    int_str = str(integral_part)
    frac_str = str(fractional_part)
    precision = len(frac_str)
    
    # Create the float from parts
    float_num = float(f"{int_str}.{frac_str}")
    
    # Format with original and double precision
    original_format = f"{float_num:.{precision}f}"
    double_format = f"{float_num:.{2*precision}f}"
    
    # Analyze the results
    expected_zeros = original_format + "0" * precision
    
    # Determine if there are rounding errors or just trailing zeros
    has_trailing_zeros = double_format == expected_zeros
    
    # Print results
    print(f"With {2*precision} digits after the decimal point, ", end="")
    
    if has_trailing_zeros:
        zero_word = "zero" if precision == 1 else "zeroes"
        print(f"{original_format} prints out with {precision} trailing {zero_word}, "
              f"namely, as {double_format}")
    else:
        print(f"{original_format} prints out as {double_format}")


def f5_4(integral_part: int, fractional_part: int) -> None:
    """
    Analyzes how floating point numbers are represented with different precisions.
    
    Uses regex to analyze the pattern of digits in the double precision representation.
    
    Args:
        integral_part: The integer part of the number
        fractional_part: The fractional part (as an integer)
    """
    import re
    
    # Calculate precision
    precision = len(str(fractional_part))
    double_precision = precision * 2
    
    # Create the float
    float_str = f"{integral_part}.{fractional_part}"
    float_val = float(float_str)
    
    # Format with different precisions
    single_precision_str = f"{float_val:.{precision}f}"
    double_precision_str = f"{float_val:.{double_precision}f}"
    
    # Start the output
    print(f"With {double_precision} digits after the decimal point, ", end="")
    
    # Check if the second half consists of all zeros
    decimal_part = double_precision_str.split('.')[1]
    pattern = re.compile(r'([0-9]+?)(' + '0' * precision + ')$')
    match = pattern.match(decimal_part)
    
    if match and len(match.group(1)) == precision:
        # The second half is all zeros
        zero_word = "zero" if precision == 1 else "zeroes"
        print(f"{single_precision_str} prints out with {precision} trailing {zero_word}, "
              f"namely, as {double_precision_str}")
    else:
        # There are rounding errors
        print(f"{single_precision_str} prints out as {double_precision_str}")