import yfinance as yf
import pandas as pd


def get_options_expirations(ticker):
    stock = yf.Ticker(ticker)
    return stock.options


def get_option_chain(ticker, date):
    stock = yf.Ticker(ticker)
    option_chain = pd.DataFrame(data=stock.option_chain(date), dtype=object)
    return option_chain


get_options_expirations("MSFT")

