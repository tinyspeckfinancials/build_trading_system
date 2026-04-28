def execute_trades(df):
    for i in range(len(df)):
        signal = df["signal"][i]
        qty = df["position_size"][i]

        if signal == 1:
            print(f"Placing BUY order: Qty={qty}")

        elif signal == -1:
            print(f"Placing SELL order: Qty={qty}")