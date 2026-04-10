import streamlit as st
import requests

st.set_page_config(page_title="Crypto Dashboard", layout="wide")

st.title("Crypto Price Dashboard")
st.caption("Live prices from CoinGecko")

url = "https://api.coingecko.com/api/v3/simple/price"
params = {"ids": "bitcoin,ethereum,solana,cardano,chainlink", "vs_currencies": "usd"}
data = requests.get(url, params=params).json()

if "bitcoin" in data and "ethereum" in data and "solana" in data and "cardano" in data and "chainlink" in data:
    col1, col2, col3 = st.columns(3)
    col1.metric("Bitcoin", f"${data['bitcoin']['usd']:,.0f}")
    col2.metric("Ethereum", f"${data['ethereum']['usd']:,.2f}")
    col3.metric("Solana", f"${data['solana']['usd']:,.2f}")

    col4, col5 = st.columns(2)
    col4.metric("Cardano", f"${data['cardano']['usd']:,.4f}")
    col5.metric("Chainlink", f"${data['chainlink']['usd']:,.2f}")
else:
    st.error("Could not fetch prices from CoinGecko. Please refresh the page.")
    