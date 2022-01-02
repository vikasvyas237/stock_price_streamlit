import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Stock Price for a Single Stock

Below graphs are the closing stock and the volume of Apple Inc.
""")

tickerSymbol = 'AAPL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = '1d' , start='2020-01-01', end='2021-12-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
