# Crypto Price Pipeline

A data pipeline that automatically collects live cryptocurrency 
prices and stores them for analysis.

## What it does
- Fetches live Bitcoin, Ethereum and Solana prices every 30 seconds 
  from the CoinGecko API
- Stores prices in a local DuckDB database with duplicate prevention
- Analyzes price history with pandas and SQL queries

## Technologies
- Python
- DuckDB
- pandas
- CoinGecko API

## How to run

Install dependencies:
pip install requests pandas duckdb

Collect prices:
python3 crypto.py

Analyze data:
python3 query.py