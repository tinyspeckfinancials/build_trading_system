def apply_risk_management(df, capital, risk_per_trade=0.01):
    df["position_size"] = 0

    for i in range(len(df)):
        if df["signal"][i] == 1:
            risk_amount = capital * risk_per_trade
            price = df["close"][i]
            quantity = int(risk_amount / price)
            df["position_size"][i] = quantity

    return df