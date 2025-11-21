"""
safe_division module - Provides a safe division function that handles division by zero
"""

def safe_division(a, b):
    """
    Safely divide two numbers, handling division by zero gracefully.
    
    Args:
        a: The numerator (dividend)
        b: The denominator (divisor)
    
    Returns:
        The result of a / b if b is not zero, otherwise returns None
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        None
        >>> safe_division(-10, 2)
        -5.0
    """
    if b == 0:
        return None
    return a / b
