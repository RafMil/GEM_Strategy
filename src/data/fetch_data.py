import yfinance as yf
import pandas as pd

def fetch_etf_data(ticker: str, start: str = "2010-01-01") -> pd.DataFrame:
    """Fetch historical data for given ETF from Yahoo Finance."""
    data = yf.download(ticker, start=start)
    return data