def validate_order_input(symbol, side, order_type, quantity, price=None):
    """
    Validates user input. Returns (True, None) if valid, 
    or (False, error_message) if invalid.
    """
    # 1. Validate Side 
    if side.upper() not in ['BUY', 'SELL']:
        return False, "Side must be 'BUY' or 'SELL'."

    # 2. Validate Order Type 
    if order_type.upper() not in ['MARKET', 'LIMIT']:
        return False, "Type must be 'MARKET' or 'LIMIT'."

    # 3. Validate Quantity
    try:
        qty = float(quantity)
        if qty <= 0:
            return False, "Quantity must be greater than 0."
    except ValueError:
        return False, "Quantity must be a number."

    # 4. Validate Price for LIMIT orders 
    if order_type.upper() == 'LIMIT':
        if not price:
            return False, "Price is required for LIMIT orders."
        try:
            p = float(price)
            if p <= 0:
                return False, "Price must be greater than 0."
        except ValueError:
            return False, "Price must be a number."

    return True, None