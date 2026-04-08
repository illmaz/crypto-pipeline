import duckdb
import pandas as pd

conn = duckdb.connect("crypto.db")

pd.set_option('display.max_columns', None)

result = conn.execute("""
    SELECT
        MIN(bitcoin) as btc_low,
        MAX(bitcoin) as btc_high,
        MAX(bitcoin) - MIN(bitcoin) as btc_movement,
        ROUND(AVG(bitcoin), 2) as btc_avg,
        MIN(ethereum) as eth_low,
        MAX(ethereum) as eth_high,
        MAX(ethereum) - MIN(ethereum) as eth_movement,
        ROUND(AVG(ethereum), 2) as eth_avg,
        MIN(solana) as sol_low,
        MAX(solana) as sol_high,
        MAX(solana) - MIN(solana) as sol_movement,
        ROUND(AVG(solana), 2) as sol_avg
    FROM prices
""").fetchdf()

print(result.T)

filtered = conn.execute("""
    SELECT *
    FROM prices
    WHERE bitcoin > 71700
""").fetchdf()

print(filtered)

btc_sorted = conn.execute("""
    SELECT timestamp, bitcoin
    FROM prices
    ORDER BY bitcoin DESC
""").fetchdf()

print(btc_sorted)

duplicates = conn.execute("""
    SELECT bitcoin, COUNT(*) as count
    FROM prices
    GROUP BY bitcoin
    HAVING COUNT(*) > 1
""").fetchdf()

print(duplicates)