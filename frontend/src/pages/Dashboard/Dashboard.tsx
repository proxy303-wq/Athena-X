import DecisionCard from "../../components/DecisionCard/DecisionCard";
import MarketCard from "../../components/MarketCard/MarketCard";
import IndicatorCard from "../../components/IndicatorCard/IndicatorCard";
import OptionCard from "../../components/OptionCard/OptionCard";
import GreeksCard from "../../components/GreeksCard/GreeksCard";
import ReasoningCard from "../../components/ReasoningCard/ReasoningCard";
import ChartCard from "../../components/ChartCard/ChartCard";

import type { DashboardResponse } from "../../types/dashboard";

type Props = {
  dashboard: DashboardResponse;
};

export default function Dashboard({ dashboard }: Props) {
  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "repeat(2, minmax(450px, 1fr))",
        gap: "24px",
        alignItems: "start",
      }}
    >
      <DecisionCard
        direction={dashboard.trade.direction}
        confidence={dashboard.trade.confidence}
        trend={dashboard.trade.trend}
        risk={dashboard.trade.risk}
      />

      <MarketCard
        market={dashboard.market.market}
        price={dashboard.market.price}
        change={dashboard.market.change}
        changePercent={dashboard.market.change_percent}
        high={dashboard.market.high}
        low={dashboard.market.low}
        open={dashboard.market.open}
        source={dashboard.market.source}
      />

      <IndicatorCard
        ema20={dashboard.analysis.indicators.ema20}
        ema50={dashboard.analysis.indicators.ema50}
        rsi={dashboard.analysis.indicators.rsi}
        vwap={dashboard.analysis.indicators.vwap}
        priceAboveEMA20={
          dashboard.analysis.indicators.price_above_ema20
        }
        ema20AboveEMA50={
          dashboard.analysis.indicators.ema20_above_ema50
        }
        priceAboveVWAP={
          dashboard.analysis.indicators.price_above_vwap
        }
      />

      <OptionCard
        pcr={dashboard.analysis.pcr.pcr}
        sentiment={dashboard.analysis.pcr.sentiment}
        support={dashboard.analysis.oi.support}
        resistance={dashboard.analysis.oi.resistance}
        maxPain={dashboard.analysis.max_pain.max_pain}
      />

      <GreeksCard
        callDelta={dashboard.analysis.greeks.call_delta}
        putDelta={dashboard.analysis.greeks.put_delta}
        gamma={dashboard.analysis.greeks.call_gamma}
        theta={dashboard.analysis.greeks.call_theta}
        iv={dashboard.analysis.greeks.call_iv}
      />

      <ReasoningCard
        reasoning={dashboard.trade.reasoning}
        direction={dashboard.trade.direction}
        confidence={dashboard.trade.confidence}
      />

      <div
        style={{
          gridColumn: "1 / span 2",
        }}
      >
        <ChartCard
          candles={dashboard.candles}
          support={dashboard.analysis.oi.support}
          resistance={dashboard.analysis.oi.resistance}
          entry={dashboard.trade.entry}
          stopLoss={dashboard.trade.stop_loss}
          target1={dashboard.trade.target1}
          target2={dashboard.trade.target2}
        />
      </div>
    </div>
  );
}