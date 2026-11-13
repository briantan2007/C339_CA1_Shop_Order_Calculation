def qualifies_free_delivery(total_cents):
    """Check whether a cart qualifies for free delivery."""
    if type(total_cents) is not int:
        raise TypeError("total must be an integer")
    
    if total_cents < 0:
        raise ValueError("total must be nonnegative")
    
    return total_cents > 5000
