import logging
from unittest.mock import patch

# Set up logging to both console and file
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(message)s',
                    handlers=[
                        logging.FileHandler('logs/trading_bot.log'),
                        logging.StreamHandler()
                    ])


def place_order(symbol, side, amount, price=None):
    """ Simulate placing a trade order """
    if side == 'buy' and symbol == 'BTC/USDT' and amount > 0:
        logging.info(f"Mock Buy Order placed for {amount} of {symbol} at price {price}.")
        return {'status': 'success', 'order_id': 'mock_order_id'}
    elif side == 'sell' and symbol == 'BTC/USDT' and amount > 0:
        logging.info(f"Mock Sell Order placed for {amount} of {symbol} at price {price}.")
        return {'status': 'success', 'order_id': 'mock_order_id'}
    else:
        logging.error(f"Failed to place order: Invalid parameters.")
        return {'status': 'error', 'message': 'Invalid parameters'}


def mock_trading():
    """ Simulate mock trading """
    logging.info("Starting mock trading session...")

    # Example mock trade logic
    symbol = 'BTC/USDT'
    buy_amount = 0.01
    sell_amount = 0.01
    buy_price = 50000  # Mock price for buy order
    sell_price = 51000  # Mock price for sell order

    # Place mock buy order
    buy_response = place_order(symbol, 'buy', buy_amount, buy_price)
    if buy_response['status'] == 'success':
        logging.info(f"Buy order successful: {buy_response}")

    # Place mock sell order
    sell_response = place_order(symbol, 'sell', sell_amount, sell_price)
    if sell_response['status'] == 'success':
        logging.info(f"Sell order successful: {sell_response}")

    logging.info("Mock trading session completed.")


# Main function to execute mock trading
if __name__ == "__main__":
    mock_trading()


