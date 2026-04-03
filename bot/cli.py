import argparse
import sys
from bot.logging_config import setup_logging
from bot.client import MockBinanceClient
from bot.validators import validate_order_input
from bot.orders import execute_trade

def main():
    # 1. Initialize Logging
    logger = setup_logging()
    
    # 2. Setup CLI Arguments 
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot (Mock Mode)")
    parser.add_argument("--symbol", type=str, required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", type=str, required=True, choices=['BUY', 'SELL'], help="BUY or SELL")
    parser.add_argument("--type", type=str, required=True, choices=['MARKET', 'LIMIT'], help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Amount to trade")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    # 3. Initialize the Client 
    client = MockBinanceClient(logger)

    # 4. Validate Input 
    is_valid, error_msg = validate_order_input(
        args.symbol, args.side, args.type, args.quantity, args.price
    )

    if not is_valid:
        logger.error(f"Validation Failed: {error_msg}")
        print(f"Error: {error_msg}")
        sys.exit(1)

    # 5. Execute Order 
    try:
        result = execute_trade(client, args.symbol, args.side, args.type, args.quantity, args.price)

        if result["success"]:
            data = result["data"]
            print("\n--- Order Response Details ---")
            print(f"Status: {data['status']}")
            print(f"Order ID: {data['orderId']}")
            print(f"Executed Qty: {data['executedQty']}")
            print(f"Avg Price: {data['avgPrice']}")
            print("\n✅ Success: Order placed successfully.")
        else:
            print(f"\n❌ Failure: {result['error']}")
            
    except Exception as e:
        logger.error(f"System Error during execution: {str(e)}")
        print(f"\n❌ Fatal Error: {str(e)}")

if __name__ == "__main__":
    main()