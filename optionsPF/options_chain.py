from datetime import timedelta
import datetime

import yfinance as yf
import pandas as pd
import numpy as np
import pytz
from pytz import timezone
from django.utils.timezone import make_aware
import math


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
    filtered_calls = calls.drop(['contractSymbol', 'lastTradeDate', 'change',
                                 'percentChange', 'inTheMoney', 'contractSize', 'currency'], axis=1)
    puts = option_chain.at[1, 0]
    filtered_puts = puts.drop(['contractSymbol', 'lastTradeDate', 'change',
                               'percentChange', 'inTheMoney', 'contractSize', 'currency'], axis=1)
    filtered_calls.replace(np.NaN, 0, inplace=True)
    filtered_puts.replace(np.NaN, 0, inplace=True)

    filtered_calls = filtered_calls.astype({'strike': np.int32, 'volume': np.int32, 'openInterest': np.int32})
    filtered_puts = filtered_puts.astype({'strike': np.int32, 'volume': np.int32, 'openInterest': np.int32})

    rounded_calls = filtered_calls.round({'bid': 2, 'ask': 2, 'impliedVolatility': 2})
    rounded_puts = filtered_puts.round({'bid': 2, 'ask': 2, 'impliedVolatility': 2})

    call_values = rounded_calls.to_numpy(dtype=object)
    put_values = rounded_puts.to_numpy(dtype=object)

    call_put = [call_values, put_values, options_strategies]
    return call_put


def get_stock_price(ticker):
    eastern = timezone('US/Eastern')
    date_time = datetime.datetime.now(tz=eastern)
    print(date_time)
    week_number = date_time.weekday()
    time = date_time.time().strftime("%H:%M")
    hour = date_time.time().strftime("%H")
    mins = date_time.time().strftime("%M")
    retrieved_date = date_time.date()
    if week_number == 5:
        date_time = date_time.date() - timedelta(days=1)
        retrieved_date = date_time
    elif week_number == 6:
        date_time = date_time.date() - timedelta(days=2)
        retrieved_date = date_time
    elif week_number == 0 and ((int(hour) < 9 and int(mins) < 35) or int(hour) < 10):
        date_time = date_time.date() - timedelta(days=3)
        retrieved_date = date_time
    elif (int(hour) < 9 and int(mins)) < 35 or int(hour) < 10:
        date_time = date_time.date() - timedelta(days=1)
        retrieved_date = date_time
        time = "16:00"
        hour = "16"
    data = yf.download(ticker, start=retrieved_date, interval="15m")
    string_time = data.index.astype(str).str[11:16]
    interval = choose_stock_interval(time, string_time)
    price_param = '{:%Y/%m/%d }'.format(date_time) + interval + '-04:00'
    if int(hour) >= 16:
        price = np.round(data.at[price_param, 'Close'], 2)
    else:
        price = np.round(data.at[price_param, 'Open'], 2)
    return price


def choose_stock_interval(time, times_column):
    current_hour = int(time.split(':')[0])
    current_mins = int(time.split(':')[1])
    if current_hour >= 16 or current_hour <= 8:
        print(times_column)
        return times_column[len(times_column)-1]
    else:
        for interval in times_column:
            hour = int(interval.split(':')[0])
            mins = int(interval.split(':')[1])
            if current_hour == hour and round_down(current_mins) == mins:
                return interval


def round_down(mins):
    if mins <= 16:
        return 0
    elif mins <= 31:
        return 15
    elif mins <= 46:
        return 30
    else:
        return 45
