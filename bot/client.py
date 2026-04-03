import time
import random
import uuid
import logging
from datetime import datetime

class MockBinanceClient:
    def __init__(self, logger):
        self.logger = logger
        self.logger.info("MOCK Binance Testnet Client Initialized (No KYC Mode)")

    def place_futures_order(self, symbol, side, order_type, quantity, price=None):
        """Simulates placing an order and returns a Binance-style JSON response."""
        try:
            self.logger.info(f"MOCK REQUEST: {side} {order_type} {quantity} {symbol} @ {price}")
            
            # Simulate network latency
            time.sleep(0.5)

            # Generate a fake order ID and execution data
            order_id = str(uuid.uuid4().int)[:10]
            avg_price = price if price else random.uniform(60000, 65000) # Fake BTC price
            
            # Standard Binance response structure 
            response = {
                "orderId": order_id,
                "symbol": symbol.upper(),
                "status": "FILLED",
                "clientOrderId": f"my_order_{order_id}",
                "price": str(price) if price else "0.0",
                "avgPrice": str(round(avg_price, 2)),
                "origQty": str(quantity),
                "executedQty": str(quantity),
                "side": side.upper(),
                "type": order_type.upper(),
                "updateTime": int(datetime.now().timestamp() * 1000)
            }

            self.logger.info(f"MOCK RESPONSE: Order {order_id} - Status: {response['status']}")
            return response

        except Exception as e:
            self.logger.error(f"Mock Client Error: {str(e)}")
            raise