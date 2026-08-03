import yfinance as yf


def get_nifty_data():
    ticker = yf.Ticker("^NSEI")

    info = ticker.fast_info

    return {
        "price": info.get("lastPrice"),
        "open": info.get("open"),
        "high": info.get("dayHigh"),
        "low": info.get("dayLow"),
        "volume": info.get("lastVolume"),
    }