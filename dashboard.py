import streamlit as st
import duckdb
import pandas as pd

st.title("Crypto Price Dashboard")

conn = duckdb.connect("crypto.db", read_only=True)

df = conn.execute("SELECT * FROM prices ORDER BY timestamp DESC").fetchdf()

latest = df.iloc[0]

col1, col2, col3 = st.columns(3)

col1.metric("Bitcoin", f"${latest['bitcoin']:,.0f}")
col2.metric("Ethereum", f"${latest['ethereum']:,.2f}")
col3.metric("Solana", f"${latest['solana']:,.2f}")

st.dataframe(df)

st.subheader("Bitcoin Price Over Time")
st.line_chart(df.set_index("timestamp")["bitcoin"])