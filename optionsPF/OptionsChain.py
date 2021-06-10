import yfinance as yf
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def get_options_expirations(ticker):
    stock = yf.Ticker(ticker)
    return stock.options


def get_option_chain(ticker, date):
    stock = yf.Ticker(ticker)
    option_chain = pd.DataFrame(data=stock.option_chain(date), dtype=object)
    calls = option_chain.at[0,0]
    puts = option_chain.at[1,0]
    html_calls = calls.to_html()
    html_puts = puts.to_html()
    call_put = [html_calls, html_puts]
    return call_put



x = get_option_chain('aapl', '2021-06-11')