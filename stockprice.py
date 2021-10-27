import yfinance as yf
import streamlit as st
from datetime import date
import datetime

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
curr_date = date.today()
tickerSymbol = st.text_input('Input the stock symbol','GOOGL')
start_date = st.date_input('Date from when you want to check',datetime.date(2010,5,31))
end_date = st.date_input('Date till you want to check',curr_date)
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start = start_date, end = end_date)
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
