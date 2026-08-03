from dataclasses import dataclass


@dataclass(frozen=True)
class Asset:
    name: str
    exchange: str
    segment: str
    trading_symbol: str
    groww_symbol: str


ASSETS = {

    "NIFTY": Asset(
        name="NIFTY 50",
        exchange="NSE",
        segment="CASH",
        trading_symbol="NIFTY",
        groww_symbol="NSE-NIFTY",
    ),

    "BANKNIFTY": Asset(
        name="NIFTY BANK",
        exchange="NSE",
        segment="CASH",
        trading_symbol="BANKNIFTY",
        groww_symbol="NSE-BANKNIFTY",
    ),

    "FINNIFTY": Asset(
        name="NIFTY FIN SERVICE",
        exchange="NSE",
        segment="CASH",
        trading_symbol="FINNIFTY",
        groww_symbol="NSE-FINNIFTY",
    ),

    "MIDCPNIFTY": Asset(
        name="NIFTY MIDCAP SELECT",
        exchange="NSE",
        segment="CASH",
        trading_symbol="MIDCPNIFTY",
        groww_symbol="NSE-MIDCPNIFTY",
    ),

    "NIFTYNXT50": Asset(
        name="NIFTY NEXT 50",
        exchange="NSE",
        segment="CASH",
        trading_symbol="NIFTYNXT50",
        groww_symbol="NSE-NIFTYNXT50",
    ),

    "SENSEX": Asset(
        name="SENSEX",
        exchange="BSE",
        segment="CASH",
        trading_symbol="SENSEX",
        groww_symbol="BSE-SENSEX",
    ),

    "BANKEX": Asset(
        name="BANKEX",
        exchange="BSE",
        segment="CASH",
        trading_symbol="BANKEX",
        groww_symbol="BSE-BANKEX",
    ),

    "CRUDEOIL": Asset(
        name="CRUDE OIL",
        exchange="MCX",
        segment="COMMODITY",
        trading_symbol="CRUDEOIL",
        groww_symbol="MCX-CRUDEOIL",
    ),

    "NATURALGAS": Asset(
        name="NATURAL GAS",
        exchange="MCX",
        segment="COMMODITY",
        trading_symbol="NATURALGAS",
        groww_symbol="MCX-NATURALGAS",
    ),

    "GOLD": Asset(
        name="GOLD",
        exchange="MCX",
        segment="COMMODITY",
        trading_symbol="GOLD",
        groww_symbol="MCX-GOLD",
    ),

    "SILVER": Asset(
        name="SILVER",
        exchange="MCX",
        segment="COMMODITY",
        trading_symbol="SILVER",
        groww_symbol="MCX-SILVER",
    ),

    "COPPER": Asset(
        name="COPPER",
        exchange="MCX",
        segment="COMMODITY",
        trading_symbol="COPPER",
        groww_symbol="MCX-COPPER",
    ),

    "ZINC": Asset(
        name="ZINC",
        exchange="MCX",
        segment="COMMODITY",
        trading_symbol="ZINC",
        groww_symbol="MCX-ZINC",
    ),
}


def get_asset(symbol: str) -> Asset:
    symbol = symbol.upper()

    if symbol not in ASSETS:
        raise ValueError(f"Unsupported Asset: {symbol}")

    return ASSETS[symbol]