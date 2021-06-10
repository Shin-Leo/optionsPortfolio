import yfinance as yf
import pandas as pd
import html

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

options_strategies = ['Covered Call', 'Married Put', 'Bull Call Spread', 'Bear Put Spread', 'Protective Collar',
                      'Long Straddle', 'Long Strangle', 'Long Call Butterfly Spread', 'Iron Condor', 'Iron Butterfly']


def get_options_expirations(ticker):
    stock = yf.Ticker(ticker)
    return stock.options


def get_option_chain(ticker, date):
    stock = yf.Ticker(ticker)
    option_chain = pd.DataFrame(data=stock.option_chain(date), dtype=object)
    calls = option_chain.at[0, 0]
    filtered_calls = calls.drop(['contractSymbol', 'lastTradeDate', 'change', 'lastPrice',
                                 'percentChange', 'inTheMoney', 'contractSize', 'currency'], axis=1)
    puts = option_chain.at[1, 0]
    filtered_puts = puts.drop(['contractSymbol', 'lastTradeDate', 'change', 'lastPrice',
                               'percentChange', 'inTheMoney', 'contractSize', 'currency'], axis=1)
    filtered_calls.set_index('strike', inplace=True)
    filtered_puts.set_index('strike', inplace=True)
    html_calls = filtered_calls.to_html()
    html_puts = filtered_puts.to_html()
    call_put = [html_calls, html_puts, options_strategies]
    return call_put
