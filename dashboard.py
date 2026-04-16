import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Crypto Intelligence Dashboard", layout="wide")

st.markdown("""
    <style>
    .main { padding: 2rem; }
    .stMetric { background: #1a1a2e; padding: 1rem; border-radius: 10px; border: 1px solid #16213e; }
    </style>
""", unsafe_allow_html=True)

st.title("Crypto Intelligence Dashboard")
st.caption(f"Live market data • Updated {datetime.now().strftime('%H:%M:%S')}")

url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin,ethereum,solana,cardano,chainlink",
    "vs_currencies": "usd",
    "include_24hr_change": "true",
    "include_market_cap": "true"
}
data = requests.get(url, params=params).json()

if "bitcoin" in data:
    st.subheader("Market Overview")
    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Bitcoin", f"${data['bitcoin']['usd']:,.0f}", 
        f"{data['bitcoin']['usd_24h_change']:.2f}%")
    col2.metric("Ethereum", f"${data['ethereum']['usd']:,.0f}", 
        f"{data['ethereum']['usd_24h_change']:.2f}%")
    col3.metric("Solana", f"${data['solana']['usd']:,.2f}", 
        f"{data['solana']['usd_24h_change']:.2f}%")
    col4.metric("Cardano", f"${data['cardano']['usd']:,.4f}", 
        f"{data['cardano']['usd_24h_change']:.2f}%")
    col5.metric("Chainlink", f"${data['chainlink']['usd']:,.2f}", 
        f"{data['chainlink']['usd_24h_change']:.2f}%")

    st.divider()

    st.subheader("Market Cap")
    col1, col2, col3 = st.columns(3)
    col1.metric("Bitcoin Market Cap", f"${data['bitcoin']['usd_market_cap']:,.0f}")
    col2.metric("Ethereum Market Cap", f"${data['ethereum']['usd_market_cap']:,.0f}")
    col3.metric("Solana Market Cap", f"${data['solana']['usd_market_cap']:,.0f}")

    st.divider()

    st.subheader("24h Performance")
    import pandas as pd
    perf_data = {
        "Coin": ["Bitcoin", "Ethereum", "Solana", "Cardano", "Chainlink"],
        "Price (USD)": [
            data['bitcoin']['usd'],
            data['ethereum']['usd'],
            data['solana']['usd'],
            data['cardano']['usd'],
            data['chainlink']['usd']
        ],
        "24h Change %": [
            round(data['bitcoin']['usd_24h_change'], 2),
            round(data['ethereum']['usd_24h_change'], 2),
            round(data['solana']['usd_24h_change'], 2),
            round(data['cardano']['usd_24h_change'], 2),
            round(data['chainlink']['usd_24h_change'], 2)
        ]
    }
    df = pd.DataFrame(perf_data)
    st.dataframe(df, use_container_width=True, hide_index=True)

else:
    st.error("Could not fetch prices. Please refresh.")