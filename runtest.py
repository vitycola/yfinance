#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Yahoo! Finance market data downloader (+fix for Pandas Datareader)
# https://github.com/ranaroussi/yfinance

"""
Sanity check for most common library uses all working

- Stock: Microsoft
- ETF: Russell 2000 Growth
- Mutual fund: Vanguard 500 Index fund
- Index: S&P500
- Currency BTC-USD
"""

from __future__ import print_function
import yfinance as yf


def test_yfinance():
    for symbol in ['MSFT', 'AAPL', 'MMM']:
        print(">>", symbol, end=' ... ')
        ticker = yf.Ticker(symbol)

        # always should have info and history for valid symbols
        assert(ticker.info is not None and ticker.info != {})
        assert(ticker.history(period="max").empty is False)

        # following should always gracefully handled, no crashes
        assert(ticker.cashflow.empty is False)
        assert(ticker.balance_sheet.empty is False)
        assert(ticker.financials.empty is False)
        assert(ticker.sustainability.empty is False)
        assert(ticker.major_holders.empty is False)
        ticker.institutional_holders

        print("OK")


if __name__ == "__main__":
    test_yfinance()
