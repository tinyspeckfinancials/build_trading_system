import pandas as pd

def calculate_moving_average(df, window=20):
    df["ma"] = df["close"].rolling(window=window).mean()
    return df

def generate_signals(df):
    df["signal"] = 0

    for i in range(1, len(df)):
        if df["close"][i] > df["ma"][i] and df["close"][i-1] <= df["ma"][i-1]:
            df["signal"][i] = 1   # Buy
        elif df["close"][i] < df["ma"][i] and df["close"][i-1] >= df["ma"][i-1]:
            df["signal"][i] = -1  # Sell

    return df