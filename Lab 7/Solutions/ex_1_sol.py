from typing import Any, Generator


def f1_1() -> Generator[None, Any, Any]:
    """
    Generates an infinite sequence of hourglass-like patterns.

    This generator function produces a repeating pattern of ASCII art segments:
    1. Top of hourglass (triangle pointing up)
    2. Horizontal line
    3. Bottom of hourglass (triangle pointing down)
    4. Vertical lines

    Each call to next() on this generator will print one segment and pause execution
    until the next call. The pattern repeats indefinitely in a cycle.

    Returns:
        A generator that yields None after printing each segment
    """
    while True:
        print(' /\\\n/  \\')
        yield
        print('----')
        yield
        print('\\  /\n \\/')
        yield
        print(' ||\n ||')
        yield


def f1_2() -> Generator[None, Any, Any]:
    """
    Generates an infinite sequence of hourglass-like patterns using a more structured approach.

    This implementation stores the pattern segments in a list and cycles through them,
    making the code more maintainable and easier to modify if the pattern needs to change.

    The pattern consists of four segments that repeat indefinitely:
    1. Top of hourglass (triangle pointing up)
    2. Horizontal line
    3. Bottom of hourglass (triangle pointing down)
    4. Vertical lines

    Returns:
        A generator that yields None after printing each segment
    """
    # Store all pattern segments in a list for better maintainability
    patterns = [
        ' /\\\n/  \\',  # Top of hourglass
        '----',      # Middle line
        '\\  /\n \\/',  # Bottom of hourglass
        ' ||\n ||'   # Vertical lines
    ]

    # Infinite loop to cycle through the patterns
    while True:
        for pattern in patterns:
            print(pattern)
            yield
