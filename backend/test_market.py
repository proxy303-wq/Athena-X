from app.groww.client import groww

df = groww.get_all_instruments()

result = df[
    df["name"].astype(str).str.contains("NIFTY", case=False, na=False)
]

print(result[[
    "exchange",
    "exchange_token",
    "trading_symbol",
    "groww_symbol",
    "name",
    "instrument_type",
    "segment"
]])