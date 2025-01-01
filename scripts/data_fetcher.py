import ccxt
import pandas as pd

# Initialize KuCoin exchange
exchange = ccxt.kucoin({
    'apiKey': '67707d910b97fd0001d94c8b',
    'secret': 'e1e99f60-b1d9-457f-a56c-ca636bbb059e',
    'password': 'Divakar&100',  # KuCoin requires a passphrase
    'rateLimit': 1200,
    'enableRateLimit': True,
})

# Function to fetch data
def fetch_data(symbol, timeframe, limit):
    """Fetch historical OHLCV data from KuCoin."""
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# Function to preprocess data
def preprocess_data(df):
    """Clean and preprocess the data."""
    df.dropna(inplace=True)  # Remove missing values
    df['close_normalized'] = (df['close'] - df['close'].min()) / (df['close'].max() - df['close'].min())  # Normalize
    return df

# Main execution
if __name__ == "__main__":
    # Parameters
    symbol = 'BTC/USDT'
    timeframe = '1h'
    limit = 500

    # Fetch and preprocess data
    print("Fetching data...")
    raw_data = fetch_data(symbol, timeframe, limit)
    print("Preprocessing data...")
    cleaned_data = preprocess_data(raw_data)

    # Save raw and cleaned data
    raw_data.to_csv('../data/btc_usdt_1h_raw.csv', index=False)
    cleaned_data.to_csv('../data/btc_usdt_1h_cleaned.csv', index=False)

    # Display a preview of the cleaned data
    print(cleaned_data.head())
