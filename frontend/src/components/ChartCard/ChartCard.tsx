import { useEffect, useRef } from "react";
import {
  createChart,
  ColorType,
  CandlestickSeries,
  LineStyle,
  type CandlestickData,
  type UTCTimestamp,
} from "lightweight-charts";

type Candle = {
  time: UTCTimestamp;
  open: number;
  high: number;
  low: number;
  close: number;
};

type Props = {
  candles: Candle[];

  support: number;
  resistance: number;

  entry: number;
  stopLoss: number;
  target1: number;
  target2: number;
};

export default function ChartCard({
  candles,
  support,
  resistance,
  entry,
  stopLoss,
  target1,
  target2,
}: Props) {
  const chartRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!chartRef.current) return;

    chartRef.current.innerHTML = "";

    const chart = createChart(chartRef.current, {
      width: chartRef.current.clientWidth,
      height: 600,

      layout: {
        background: {
          type: ColorType.Solid,
          color: "#0f172a",
        },
        textColor: "#CBD5E1",
      },

      grid: {
        vertLines: {
          color: "#1e293b",
        },
        horzLines: {
          color: "#1e293b",
        },
      },

      rightPriceScale: {
        borderColor: "#334155",
      },

      timeScale: {
        borderColor: "#334155",
      },
    });

    // ============================
    // Candles
    // ============================

    const candleSeries = chart.addSeries(CandlestickSeries);

    candleSeries.setData(
      candles.map(
        (c): CandlestickData<UTCTimestamp> => ({
          time: c.time,
          open: c.open,
          high: c.high,
          low: c.low,
          close: c.close,
        })
      )
    );

    // ============================
    // Support
    // ============================

    candleSeries.createPriceLine({
      price: support,
      color: "#22c55e",
      lineWidth: 2,
      lineStyle: LineStyle.Dashed,
      axisLabelVisible: true,
      title: "Support",
    });

    // ============================
    // Resistance
    // ============================

    candleSeries.createPriceLine({
      price: resistance,
      color: "#ef4444",
      lineWidth: 2,
      lineStyle: LineStyle.Dashed,
      axisLabelVisible: true,
      title: "Resistance",
    });

    // ============================
    // Entry
    // ============================

    candleSeries.createPriceLine({
      price: entry,
      color: "#ffffff",
      lineWidth: 3,
      axisLabelVisible: true,
      title: "ENTRY",
    });

    // ============================
    // Stop Loss
    // ============================

    candleSeries.createPriceLine({
      price: stopLoss,
      color: "#dc2626",
      lineWidth: 2,
      axisLabelVisible: true,
      title: "STOP",
    });

    // ============================
    // Target 1
    // ============================

    candleSeries.createPriceLine({
      price: target1,
      color: "#3b82f6",
      lineWidth: 2,
      axisLabelVisible: true,
      title: "TARGET 1",
    });

    // ============================
    // Target 2
    // ============================

    candleSeries.createPriceLine({
      price: target2,
      color: "#8b5cf6",
      lineWidth: 2,
      axisLabelVisible: true,
      title: "TARGET 2",
    });

    chart.timeScale().fitContent();

    const resize = () => {
      if (!chartRef.current) return;

      chart.applyOptions({
        width: chartRef.current.clientWidth,
      });
    };

    window.addEventListener("resize", resize);

    return () => {
      window.removeEventListener("resize", resize);
      chart.remove();
    };
  }, [
    candles,
    support,
    resistance,
    entry,
    stopLoss,
    target1,
    target2,
  ]);

  return (
    <div
      style={{
        background: "#1e293b",
        borderRadius: 20,
        padding: 24,
        boxShadow: "0 10px 30px rgba(0,0,0,.25)",
      }}
    >
      <h2
        style={{
          color: "#ffffff",
          marginBottom: 20,
        }}
      >
        📈 Athena X Professional Trading Chart
      </h2>

      <div
        ref={chartRef}
        style={{
          width: "100%",
          height: 600,
        }}
      />
    </div>
  );
}