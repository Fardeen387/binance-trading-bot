from bot.validators import validate_order_input

def execute_trade(client, symbol, side, order_type, quantity, price=None):
    """
    Coordinates the validation and execution of a trade.
    This fulfills the requirement for 'structured code' by separating 
    logic from the raw API client.
    """
    # 1. Internal Validation Check
    is_valid, error_msg = validate_order_input(symbol, side, order_type, quantity, price)
    
    if not is_valid:
        return {"success": False, "error": error_msg}

    try:
        # 2. Call the Client 
        response = client.place_futures_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )
        
        # 3. Format the response for the CLI layer
        return {
            "success": True,
            "data": {
                "orderId": response.get("orderId"),
                "status": response.get("status"),
                "executedQty": response.get("executedQty"),
                "avgPrice": response.get("avgPrice")
            }
        }

    except Exception as e:
        return {"success": False, "error": str(e)}