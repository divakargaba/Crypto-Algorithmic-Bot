import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Use a compatible Matplotlib backend
import matplotlib

matplotlib.use("TkAgg")


def calculate_moving_averages(dataframe, short_window, long_window):
    """Calculate short and long moving averages."""
    dataframe['Short_MA'] = dataframe['Close'].rolling(window=short_window).mean()
    dataframe['Long_MA'] = dataframe['Close'].rolling(window=long_window).mean()
    return dataframe['Short_MA'], dataframe['Long_MA']


def backtest_strategy(dataframe, short_ma, long_ma, buy_threshold, sell_threshold):
    """Backtest a moving average crossover strategy."""
    initial_balance = 10000
    balance = initial_balance
    position = 0  # 0 indicates no position, 1 indicates a long position
    trade_history = []

    for i in range(len(dataframe)):
        # Fix FutureWarning by using .iloc
        if i == 0 or pd.isna(short_ma.iloc[i]) or pd.isna(long_ma.iloc[i]):
            continue

        # Buy Signal
        if short_ma.iloc[i] > long_ma.iloc[i] * (1 + buy_threshold):
            if position == 0:  # Only buy if not already holding
                position = balance / dataframe['Close'].iloc[i]
                balance = 0
                trade_history.append(f"Buy at {dataframe['Close'].iloc[i]}")

        # Sell Signal
        elif short_ma.iloc[i] < long_ma.iloc[i] * (1 - sell_threshold):
            if position > 0:  # Only sell if holding a position
                balance = position * dataframe['Close'].iloc[i]
                position = 0
                trade_history.append(f"Sell at {dataframe['Close'].iloc[i]}")

    # Final liquidation if still holding
    if position > 0:
        balance = position * dataframe['Close'].iloc[-1]
        trade_history.append(f"Final Sell at {dataframe['Close'].iloc[-1]}")

    profit = balance - initial_balance
    return trade_history, profit


def optimize_strategy(dataframe):
    """Optimize moving average strategy parameters."""
    best_profit = -np.inf
    best_params = None

    # Try different parameter values
    for short_window in [5, 10, 20]:
        for long_window in [20, 50, 100]:
            for buy_threshold in [0.01, 0.02, 0.03]:
                for sell_threshold in [0.01, 0.03, 0.05]:
                    short_ma, long_ma = calculate_moving_averages(dataframe, short_window, long_window)
                    trade_history, profit = backtest_strategy(dataframe, short_ma, long_ma, buy_threshold,
                                                              sell_threshold)
                    if profit > best_profit:
                        best_profit = profit
                        best_params = (short_window, long_window, buy_threshold, sell_threshold)

    print(f"Best Parameters: {best_params}, Profit: {best_profit}")
    return best_params


def plot_data_with_indicators(dataframe, short_ma, long_ma):
    """Plot the price and moving averages."""
    plt.figure(figsize=(12, 6))
    plt.plot(dataframe['Close'], label='Close Price', alpha=0.5)
    plt.plot(short_ma, label='Short MA', color='orange')
    plt.plot(long_ma, label='Long MA', color='green')
    plt.title('Price and Moving Averages')
    plt.legend()

    # Save the plot instead of showing it
    plt.savefig("output_plot.png")
    print("Plot saved as output_plot.png")


if __name__ == "__main__":
    # Example data (replace this with your real data)
    data = {
        'Close': [100 + np.sin(i / 5) * 10 + np.random.normal(0, 2) for i in range(300)]
    }
    dataframe = pd.DataFrame(data)

    print("Optimizing strategy...")
    best_params = optimize_strategy(dataframe)

    # Use the best parameters found from optimization
    short_window, long_window, buy_threshold, sell_threshold = best_params
    short_ma, long_ma = calculate_moving_averages(dataframe, short_window, long_window)
    trade_history, profit = backtest_strategy(dataframe, short_ma, long_ma, buy_threshold, sell_threshold)

    print("Trade History:")
    for trade in trade_history:
        print(trade)

    print(f"Final Profit: {profit}")

    print("Visualizing data with indicators...")
    plot_data_with_indicators(dataframe, short_ma, long_ma)






