from app.groww.client import groww
import pandas as pd

print("=" * 80)
print("ATHENA X - FNO INSTRUMENT LOOKUP")
print("=" * 80)

# Download instrument master
df = groww.get_all_instruments()

print("\nColumns:")
print(df.columns)

print("\nTotal Instruments:", len(df))

# -------------------------------------------------------
# NIFTY UNDERLYING
# -------------------------------------------------------

print("\n" + "=" * 80)
print("UNDERLYING = NIFTY")
print("=" * 80)

nifty = df[
    (df["underlying_symbol"] == "NIFTY")
]

print(nifty[[
    "exchange",
    "segment",
    "underlying_symbol",
    "trading_symbol",
    "groww_symbol",
    "expiry_date",
    "instrument_type",
    "strike_price"
]].head(30))

# -------------------------------------------------------
# SEARCH BY TRADING SYMBOL
# -------------------------------------------------------

print("\n" + "=" * 80)
print("TRADING SYMBOL CONTAINS NIFTY")
print("=" * 80)

contains = df[
    df["trading_symbol"].astype(str).str.contains(
        "NIFTY",
        case=False,
        na=False
    )
]

print(contains[[
    "exchange",
    "segment",
    "underlying_symbol",
    "trading_symbol",
    "groww_symbol",
    "expiry_date",
    "instrument_type",
    "strike_price"
]].head(50))

# -------------------------------------------------------
# SEARCH BY GROWW SYMBOL
# -------------------------------------------------------

print("\n" + "=" * 80)
print("GROWW SYMBOL CONTAINS NIFTY")
print("=" * 80)

contains2 = df[
    df["groww_symbol"].astype(str).str.contains(
        "NIFTY",
        case=False,
        na=False
    )
]

print(contains2[[
    "exchange",
    "segment",
    "underlying_symbol",
    "trading_symbol",
    "groww_symbol",
    "expiry_date",
    "instrument_type",
    "strike_price"
]].head(50))