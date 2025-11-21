def safe_division(a, b) -> float | None:
    """
    Safely divide two numbers, preventing division by zero.
    
    Args:
        a: The dividend (numerator)
        b: The divisor (denominator)
    
    Returns:
        float: The result of a / b if b is not zero
        None: If b is zero
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> result = safe_division(10, 0)
        >>> result is None
        True
        >>> safe_division(7, 3)
        2.3333333333333335
    """
    if b == 0:
        return None
    return a / b
