import pandas as pd

def run_backtest(df, initial_capital=100000):
    capital = initial_capital
    position = 0
    entry_price = 0

    trade_log = []

    for i in range(len(df)):
        signal = df["signal"][i]
        price = df["close"][i]

        if signal == 1 and position == 0:
            position = 1
            entry_price = price
            trade_log.append(("BUY", price))

        elif signal == -1 and position == 1:
            profit = price - entry_price
            capital += profit
            position = 0
            trade_log.append(("SELL", price, profit))

    return capital, trade_log