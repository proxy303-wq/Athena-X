from datetime import datetime

import pandas as pd
import yfinance as yf

from .models import MarketContext


class MarketContextService:
    """
    Loads and prepares live market data for Athena.
    Every analyzer will receive the same MarketContext object.
    """

    @staticmethod
    def load(symbol: str = "^NSEI", interval: str = "5m") -> MarketContext:

        # Download latest candle data
        df = yf.download(
            symbol,
            period="5d",
            interval=interval,
            progress=False,
            auto_adjust=False,
            multi_level_index=True,
        )

        # Flatten MultiIndex columns if Yahoo returns them
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        # Remove Adjusted Close if present
        if "Adj Close" in df.columns:
            df.drop(columns=["Adj Close"], inplace=True)

        # Remove rows with missing values
        df = df.dropna()

        if df.empty:
            raise ValueError("No market data received from Yahoo Finance.")

        # Convert numeric columns
        numeric_columns = ["Open", "High", "Low", "Close", "Volume"]

        for column in numeric_columns:
            if column in df.columns:
                df[column] = pd.to_numeric(df[column], errors="coerce")

        # Drop NaNs created during conversion
        df = df.dropna()

        # Latest market price
        latest_price = float(df["Close"].iloc[-1])

        return MarketContext(
            symbol=symbol,
            timeframe=interval,
            timestamp=datetime.now(),
            current_price=latest_price,
            candles=df,
        )