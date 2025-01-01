import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('TkAgg')  # Use TkAgg backend for matplotlib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


# Function to fetch stock data
def fetch_data(ticker, start_date='2010-01-01', end_date='2024-12-31'):
    print(f"Fetching data for {ticker}...")
    data = yf.download(ticker, start=start_date, end=end_date)

    if 'Adj Close' not in data.columns:
        print("No 'Adj Close' column found, using 'Close' column instead.")
        data['Adj Close'] = data['Close']

    data['returns'] = data['Adj Close'].pct_change()
    data['SMA_50'] = data['Adj Close'].rolling(window=50).mean()
    data['SMA_200'] = data['Adj Close'].rolling(window=200).mean()
    data['RSI'] = compute_rsi(data['Adj Close'])
    data['MACD'] = compute_macd(data['Adj Close'])

    data.dropna(inplace=True)
    print(f"Fetched data for {ticker} from {start_date} to {end_date}.")
    return data


# Function to compute RSI
def compute_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi


# Function to compute MACD
def compute_macd(series, fast_period=12, slow_period=26, signal_period=9):
    macd = series.ewm(span=fast_period, adjust=False).mean() - series.ewm(span=slow_period, adjust=False).mean()
    signal = macd.ewm(span=signal_period, adjust=False).mean()
    return macd - signal


# Function to prepare the data
def prepare_data(data):
    X = data[['returns', 'SMA_50', 'SMA_200', 'RSI', 'MACD']]
    y = np.where(data['returns'].shift(-1) > 0, 1, 0)  # 1 for price increase, 0 for price decrease
    return X, y


# Function to train and evaluate model
def train_and_evaluate_model(data):
    X, y = prepare_data(data)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train Random Forest Classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate model
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy: {accuracy}")

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Cross-validation scores
    cross_val_scores = cross_val_score(model, X, y, cv=5)
    print(f"\nCross-validation scores: {cross_val_scores}")
    print(f"Mean cross-validation score: {cross_val_scores.mean()}")

    # Plot feature importances
    feature_importances = model.feature_importances_
    feature_names = ['returns', 'SMA_50', 'SMA_200', 'RSI', 'MACD']

    # Plot the feature importances
    plt.figure(figsize=(10, 6))
    plt.barh(feature_names, feature_importances)
    plt.xlabel('Feature Importance')
    plt.ylabel('Feature')
    plt.title('Feature Importances')

    # Save the plot
    plt.savefig('feature_importances.png')
    plt.show()  # Show plot


# Main function
def main():
    ticker = 'AAPL'
    data = fetch_data(ticker)
    print("\nTraining and evaluating model...")
    train_and_evaluate_model(data)


# Run the main function
if __name__ == "__main__":
    main()


