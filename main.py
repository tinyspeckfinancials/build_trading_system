from src import data_layer, signal_layer, backtest_layer, risk_layer, execution_layer
import config

# Step 1: Load Data
df = data_layer.load_csv_data("data/raw_data.csv")

# Step 2: Generate Signals
df = signal_layer.calculate_moving_average(df)
df = signal_layer.generate_signals(df)

# Step 3: Apply Risk Management
df = risk_layer.apply_risk_management(df, config.INITIAL_CAPITAL, config.RISK_PER_TRADE)

# Step 4: Backtest
final_capital, trades = backtest_layer.run_backtest(df, config.INITIAL_CAPITAL)

print("Final Capital:", final_capital)
print("Trades:", trades)

# Step 5: Execute (Paper Mode)
execution_layer.execute_trades(df)