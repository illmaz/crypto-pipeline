import requests
import duckdb
from datetime import datetime
import time

conn = duckdb.connect("crypto.db")

conn.execute("""
    CREATE TABLE IF NOT EXISTS prices (
        timestamp VARCHAR PRIMARY KEY,
        bitcoin DOUBLE,
        ethereum DOUBLE,
        solana DOUBLE
    )
""")

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum,solana",
    "vs_currencies": "usd"
}

while True:
    response = requests.get(url, params=params)
    data = response.json()

    if "bitcoin" in data and "ethereum" in data and "solana" in data:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        try:
            conn.execute("""
                INSERT INTO prices (timestamp, bitcoin, ethereum, solana)
                VALUES (?, ?, ?, ?)
            """, [now, data["bitcoin"]["usd"], data["ethereum"]["usd"], data["solana"]["usd"]])
            print(f"Saved at {now}")
        except:
            print(f"Duplicate skipped at {now}")
    else:
        print(f"API returned incomplete data, skipping...")

    time.sleep(30)