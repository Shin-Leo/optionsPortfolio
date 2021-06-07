import yfinance as yf
import pandas as pd


def get_option_chain(ticker):
    stock = yf.Ticker(ticker)
    option_chain = pd.DataFrame(data=stock.option_chain('2021-06-11'), dtype=object)
    return option_chain
