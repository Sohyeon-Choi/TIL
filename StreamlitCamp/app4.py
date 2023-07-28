import plotly.graph_objects as go 
import pandas as pd 
import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

def main():
    st.title("주식 데이터")
    st.sidebar.title("Stock Chart")
    ticker = st.sidebar.text_input("Enter a ticker (e. g. AAPL)", value="AAPL")
    # ticker = st.text_input("Enter a ticker (e. g. AAPL)", value="AAPL")
    st.sidebar.markdown('Tickers Link : [All Stock Symbols](https://stockanalysis.com/stocks/)')
    start_date = st.sidebar.date_input("시작 날짜: ", value=pd.to_datetime("2019-01-01"))
    end_date = st.sidebar.date_input("종료 날짜: ", value=pd.to_datetime("today"))

    data = yf.download(ticker, start=start_date, end=end_date)
    st.dataframe(data)

    # Line Chart, Candlestick 
    chart_type = st.sidebar.radio("Select Chart Type", ("Candlestick", "Line")) 
    candlestick = go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'])
    line = go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close')

    if chart_type == "Candlestick":
        fig = go.Figure(candlestick)
    elif chart_type == "Line":
        fig = go.Figure(line) 
    else:
        st.error("error")
    
    fig.update_layout(title=f"{ticker} Stock {chart_type} Chart", xaxis_title="Date", yaxis_title="Price")
    st.plotly_chart(fig)

    st.markdown("<hr>", unsafe_allow_html=True)
    num_row = st.sidebar.number_input("Number of Rows", min_value=1, max_value=len(data))
    st.dataframe(data[-num_row:].reset_index().sort_index(ascending=False).set_index("Date"))
    st.dataframe(num_row)
    st.write(num_row)
    st.dataframe(data[-num_row:].reset_index().sort_index(ascending=False).set)
if __name__ == "__main__":
    main()