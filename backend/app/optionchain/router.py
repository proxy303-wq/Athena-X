from fastapi import APIRouter, HTTPException

from app.assets.registry import get_asset
from app.options.service import OptionService
from app.options.parser import OptionParser
from app.optionchain.service import OptionChainService

router = APIRouter(
    prefix="/optionchain",
    tags=["Option Chain"],
)


@router.get("/{symbol}")
def option_chain(symbol: str):
    try:
        asset = get_asset(symbol)

        expiry, raw = OptionService.get_first_working_chain(asset)

        chain = OptionParser.parse(
            raw,
            asset.trading_symbol,
            expiry,
        )

        print("=" * 60)
        print(f"Expiry: {expiry}")
        print(f"Spot Price: {chain.spot_price}")
        print(f"Parsed strikes: {len(chain.strikes)}")
        print("=" * 60)

        return OptionChainService.build(chain)

    except Exception as e:
        import traceback
        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )