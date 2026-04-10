import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Crypto Dashboard", layout="wide")

st.title("Crypto Price Dashboard")
st.caption("Live prices from CoinGecko")

url = "https://api.coingecko.com/api/v3/simple/price"
params = {"ids": "bitcoin,ethereum,solana", "vs_currencies": "usd"}
data = requests.get(url, params=params).json()

col1, col2, col3 = st.columns(3)
col1.metric("Bitcoin", f"${data['bitcoin']['usd']:,.0f}")
col2.metric("Ethereum", f"${data['ethereum']['usd']:,.2f}")
col3.metric("Solana", f"${data['solana']['usd']:,.2f}")