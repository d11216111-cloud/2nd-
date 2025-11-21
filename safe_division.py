"""
A module containing a safe division function that handles division by zero.
"""

from typing import Union


def safe_division(numerator: float, denominator: float) -> Union[float, None]:
    """
    Safely divide two numbers, handling division by zero.
    
    Args:
        numerator: The number to be divided (dividend)
        denominator: The number to divide by (divisor)
    
    Returns:
        float: The result of the division if denominator is not zero.
        None: If denominator is zero.
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        None
        >>> safe_division(-10, 2)
        -5.0
    """
    if denominator == 0:
        return None
    return numerator / denominator
