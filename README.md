# Crypto-Algorithmic-Bot
# Algorithmic Trading Bot

## Overview
This project involves the development of an **algorithmic trading bot** that uses Python to implement a **moving average crossover strategy**. The bot is built to analyze and execute trades based on market data, with performance metrics and strategy evaluation achieved through **backtesting** and **real-time market simulations**.

Additionally, a **Flask-based dashboard** has been created to essentially visualize trading metrics, and **machine learning models** have been integrated to enhance the bot's prediction capabilities and improving strategy accuracy.

## Key Features

- **Moving Average Crossover Strategy**: Utilizes a common trading strategy involving the crossover of short-term and long-term moving averages to generate buy and sell signals.
  
- **Backtesting & Simulation**: Simulates the trading strategy's performance using historical market data to evaluate its potential effectiveness before live deployment.
  
- **Machine Learning Integration**: Implements machine learning models like **Random Forest** and **Logistic Regression** to predict market trends, adapting the trading strategy to changing market conditions.

- **Real-Time Data Visualization**: Built a **dynamic Flask dashboard** that uses **Jinja2** and **Plotly** to display live market data, trading performance, and real-time strategy insights for decision-making.

## Technologies Used

- **Python**: Core language for developing the trading bot and machine learning models.
- **Pandas** & **NumPy**: For data manipulation, analysis, and calculation of moving averages and other metrics.
- **Flask**: Web framework to serve the real-time dashboard.
- **Jinja2**: Templating engine used to render dynamic HTML content on the dashboard.
- **Plotly**: Library used to create interactive charts and graphs to visualize market data and performance metrics.
- **Scikit-Learn**: For implementing machine learning models like Random Forest and Logistic Regression.
  
## Performance Metrics

- **Simulated ROI**: Achieved a simulated ROI improvement of **5.3%** through backtesting with the moving average crossover strategy.
- **Market Predictions**: Machine learning models showed an improvement in prediction accuracy, enhancing the bot’s adaptability to market conditions.

## Getting Started

### Prerequisites
Before you begin,please make sure you have the following tools installed:
- Python 3.x
- Flask
- Pandas
- NumPy
- Scikit-learn
- Plotly

You can install the required dependencies using **pip**:

```bash
pip install -r requirements.txt
Running the Bot
Clone this repository:
git clone https://github.com/divakargaba/Crypto-Algorithmic-Bot.git
Navigate to the project directory:
cd Crypto-Algorithmic-Bot
Run the Flask application:
python app.py

Open the web dashboard in your browser:
Navigate to http://127.0.0.1:5000/ to see the real-time market data and trading metrics.

Backtesting
To backtest the trading strategy with historical data, run the following script:
python backtest.py
This will execute the moving average crossover strategy on historical data and output performance metrics such as ROI, drawdown, and trade statistics.

Machine Learning Models
The machine learning models (Random Forest, Logistic Regression) are integrated to predict market trends based on historical price data. To train the models and make predictions:
python train_model.py
