def calculate_total(unit_price_cents, quantity):
    """Calculate the total price of a cart in cents."""
    if type(unit_price_cents) is not int or type(quantity) is not int:
        raise TypeError("price and quantity must be integers")
    
    if unit_price_cents < 0 or quantity < 0:
        raise ValueError("price and quantity must be nonnegative")
    
    return unit_price_cents * max(quantity, 1)
