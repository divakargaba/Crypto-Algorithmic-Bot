import matplotlib

matplotlib.use('TkAgg')  # Use the TkAgg backend to avoid backend issues in PyCharm

import pandas as pd
import matplotlib.pyplot as plt


# Step 1: Load Cleaned Data
def load_data(filepath):
    """Load the cleaned historical data."""
    data = pd.read_csv(filepath)
    data['timestamp'] = pd.to_datetime(data['timestamp'])  # Ensure timestamps are datetime objects
    return data


# Step 2: Calculate Moving Averages
def calculate_moving_averages(data, short_window=20, long_window=100):
    """Calculate short-term and long-term moving averages."""
    data['short_ma'] = data['close'].rolling(window=short_window).mean()
    data['long_ma'] = data['close'].rolling(window=long_window).mean()
    return data


# Step 3: Generate Buy/Sell Signals (Simple MA Crossover)
def generate_signals(data):
    """Generate buy (1) and sell (-1) signals based on moving average crossover."""
    data['signal'] = 0
    data.loc[data['short_ma'] > data['long_ma'], 'signal'] = 1  # Buy signal
    data.loc[data['short_ma'] < data['long_ma'], 'signal'] = -1  # Sell signal
    return data


# Step 4: Simulate Trades
def simulate_trades(data):
    """Simulate trades based on the buy/sell signals."""
    data['position'] = data['signal'].shift()  # Shift signals to align with trading periods
    data['returns'] = data['position'] * data['close'].pct_change()  # Calculate returns
    total_returns = data['returns'].sum()
    num_trades = data['signal'].diff().abs().sum() / 2  # Count buy/sell pairs
    return total_returns, int(num_trades)


# Step 5: Visualize Results
def plot_strategy(data):
    """Plot the strategy's performance with buy/sell signals."""
    plt.figure(figsize=(14, 8))

    # Plot the price data
    plt.plot(data['timestamp'], data['close'], label='Close Price', alpha=0.5)

    # Plot moving averages
    plt.plot(data['timestamp'], data['short_ma'], label='Short MA (20)', alpha=0.7)
    plt.plot(data['timestamp'], data['long_ma'], label='Long MA (100)', alpha=0.7)

    # Highlight buy/sell signals
    buy_signals = data[data['signal'] == 1]
    sell_signals = data[data['signal'] == -1]
    plt.scatter(buy_signals['timestamp'], buy_signals['close'], label='Buy Signal', marker='^', color='green', alpha=1)
    plt.scatter(sell_signals['timestamp'], sell_signals['close'], label='Sell Signal', marker='v', color='red', alpha=1)

    plt.title('Optimized MA Crossover Strategy')
    plt.xlabel('Timestamp')
    plt.ylabel('Close Price')
    plt.legend()
    plt.show()


# Main Execution
if __name__ == "__main__":
    # Filepath to cleaned data
    filepath = '../notebooks/data/btc_usdt_1h_cleaned.csv'

    # Step 1: Load Data
    print("Loading data...")
    data = load_data(filepath)

    # Step 2: Calculate Indicators
    print("Calculating moving averages...")
    data = calculate_moving_averages(data)

    # Step 3: Generate Signals
    print("Generating signals...")
    data = generate_signals(data)

    # Step 4: Simulate Trades
    print("Simulating trades...")
    total_returns, num_trades = simulate_trades(data)
    print(f"Total Returns: {total_returns:.2%}")
    print(f"Number of Trades: {num_trades}")

    # Step 5: Visualize Results
    print("Visualizing strategy...")
    plot_strategy(data)



