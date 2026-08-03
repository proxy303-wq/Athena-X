import pandas as pd
import yfinance as yf

from app.context.service import MarketContextService


def debug_yfinance():
    print("=" * 60)
    print("DOWNLOADING NIFTY DATA...")
    print("=" * 60)

    df = yf.download(
        "^NSEI",
        period="5d",
        interval="5m",
        progress=False,
        auto_adjust=False
    )

    print("\nColumns:")
    print(df.columns)

    print("\nColumn Type:")
    print(type(df.columns))

    # Flatten MultiIndex if required
    if isinstance(df.columns, pd.MultiIndex):
        print("\nFlattening MultiIndex columns...")
        df.columns = df.columns.get_level_values(0)

    print("\nFinal Columns:")
    print(df.columns)

    print("\nLatest 5 Candles:")
    print(df.tail())

    print("\nLatest Close Price:")
    print(float(df["Close"].iloc[-1]))


def test_market_context():
    print("\n" + "=" * 60)
    print("TESTING MARKET CONTEXT")
    print("=" * 60)

    context = MarketContextService.load()

    print(f"Symbol        : {context.symbol}")
    print(f"Timeframe     : {context.timeframe}")
    print(f"Current Price : {context.current_price}")
    print(f"Timestamp     : {context.timestamp}")

    print("\nLast 5 Candles:")
    print(context.candles.tail())


if __name__ == "__main__":
    debug_yfinance()
    test_market_context()