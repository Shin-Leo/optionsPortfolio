import yfinance as yf
import pandas as pd
import numpy as np

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
    np.set_printoptions(suppress=True)

    stock = yf.Ticker(ticker)
    option_chain = pd.DataFrame(data=stock.option_chain(date))
    calls = option_chain.at[0, 0]
    filtered_calls = calls.drop(['contractSymbol', 'lastTradeDate', 'change', 'lastPrice',
                                 'percentChange', 'inTheMoney', 'contractSize', 'currency'], axis=1)
    puts = option_chain.at[1, 0]
    filtered_puts = puts.drop(['contractSymbol', 'lastTradeDate', 'change', 'lastPrice',
                               'percentChange', 'inTheMoney', 'contractSize', 'currency'], axis=1)
    filtered_calls.replace(np.NaN, 0, inplace=True)
    filtered_puts.replace(np.NaN, 0, inplace=True)

    filtered_calls = filtered_calls.astype({'strike': np.int32, 'volume': np.int32, 'openInterest': np.int32})
    filtered_calls = filtered_calls.astype({'strike': np.int32, 'volume': np.int32, 'openInterest': np.int32})

    rounded_calls = filtered_calls.round({'bid': 2, 'ask': 2, 'impliedVolatility': 2})
    rounded_puts = filtered_puts.round({'bid': 2, 'ask': 2, 'impliedVolatility': 2})

    call_values = rounded_calls.to_numpy(dtype=object)
    put_values = rounded_puts.to_numpy(dtype=object)

    call_put = [call_values, put_values, options_strategies]
    return call_put
