import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="📈 Stock Price Viewer", layout="centered")

# Title
st.title("📊 Stock Price Viewer")

# Stock symbol input
stock = st.text_input("Enter Stock Symbol (e.g. AAPL, TSLA, RELIANCE.NS):", "AAPL")

# Date range selection
col1, col2 = st.columns(2)
with col1:
    start = st.date_input("Start Date", pd.to_datetime("2022-01-01"))
with col2:
    end = st.date_input("End Date", pd.to_datetime("2023-01-01"))

# Fetch and display data
if st.button("📥 Get Data"):
    if stock.strip() == "":
        st.warning("⚠️ Please enter a valid stock symbol.")
    else:
        try:
            data = yf.download(stock, start=start, end=end)
            if data.empty:
                st.error("No data found. Check the stock symbol or date range.")
            else:
                st.success(f"Showing results for: {stock}")
                st.dataframe(data.tail())

                # Plot closing price
                st.subheader("📉 Closing Price Over Time")
                fig, ax = plt.subplots()
                ax.plot(data.index, data['Close'], color='blue')
                ax.set_title(f"{stock.upper()} Closing Price")
                ax.set_xlabel("Date")
                ax.set_ylabel("Price")
                ax.grid(True)
                st.pyplot(fig)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
