import pandas as pd

df = pd.read_csv("prices.csv")

print(df)
print(f"Bitcoin lowest: ${df['bitcoin'].min()}")
print(f"Ethereum average: ${df['ethereum'].mean():.2f}")
print(f"Solana highest: ${df['solana'].max()}")

df["bitcoin"].max() - df["bitcoin"].min()

print(f"Bitcoin movement: ${df['bitcoin'].max() - df['bitcoin'].min()}")
print(f"Ethereum movement: ${df['ethereum'].max() - df['ethereum'].min():.2f}")
print(f"Solana movement: ${df['solana'].max() - df['solana'].min():.2f}")

(df["bitcoin"].max() - df["bitcoin"].min()) / df["bitcoin"].min() * 100
(df["ethereum"].max() - df["ethereum"].min()) / df["ethereum"].min() * 100
(df["solana"].max() - df["solana"].min()) / df["solana"].min() * 100


print(f"Bitcoin percentage movement: {(df['bitcoin'].max() - df['bitcoin'].min()) / df['bitcoin'].min() * 100:.2f}%")
print(f"Ethereum percentage movement: {(df['ethereum'].max() - df['ethereum'].min()) / df['ethereum'].min() * 100:.2f}%")
print(f"Solana percentage movement: {(df['solana'].max() - df['solana'].min()) / df['solana'].min() * 100:.2f}%")