import type { UTCTimestamp } from "lightweight-charts";

export interface DashboardResponse {
  market: {
    market: string;
    price: number;
    change: number;
    change_percent: number;
    high: number;
    low: number;
    open: number;
    volume: number | null;
    source: string;
    timestamp: string;
  };

  candles: {
    time: UTCTimestamp;

    open: number;
    high: number;
    low: number;
    close: number;

    ema20: number;
    ema50: number;
    vwap: number;
  }[];

  analysis: {
    atm: {
      spot: number;
      atm_strike: number;
      nearby_strikes: number[];
    };

    pcr: {
      total_call_oi: number;
      total_put_oi: number;
      pcr: number;
      sentiment: string;
    };

    oi: {
      support: number;
      resistance: number;
    };

    max_pain: {
      max_pain: number;
      total_loss: number;
    };

    greeks: {
      strike: number;

      call_delta: number;
      call_gamma: number;
      call_theta: number;
      call_vega: number;
      call_iv: number;

      put_delta: number;
      put_gamma: number;
      put_theta: number;
      put_vega: number;
      put_iv: number;
    };

    indicators: {
      price: number;
      ema20: number;
      ema50: number;
      rsi: number;
      vwap: number;

      price_above_ema20: boolean;
      ema20_above_ema50: boolean;
      price_above_vwap: boolean;
    };
  };

  trade: {
    direction: string;
    confidence: number;
    trend: string;
    setup: string;
    risk: string;

    entry: number;
    stop_loss: number;
    target1: number;
    target2: number;

    reasoning: string[];
  };
}