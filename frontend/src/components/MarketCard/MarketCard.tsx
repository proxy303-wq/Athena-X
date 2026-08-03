import MetricCard from "../MetricCard/MetricCard";

type Props = {
  market: string;
  price: number;
  change: number | null;
  changePercent: number | null;
  high: number;
  low: number;
  open: number;
  source: string;
};

export default function MarketCard({
  market,
  price,
  change,
  changePercent,
  high,
  low,
  open,
  source,
}: Props) {
  const positive = (change ?? 0) >= 0;

  return (
    <div
      style={{
        background: "#1e293b",
        borderRadius: "16px",
        padding: "24px",
        width: "100%",
      }}
    >
      <h2>Market</h2>

      <h1
        style={{
          marginTop: "16px",
          fontSize: "34px",
        }}
      >
        {market}
      </h1>

      <h2
        style={{
          marginTop: "8px",
          fontSize: "30px",
        }}
      >
        {price.toFixed(2)}
      </h2>

      <p
        style={{
          color: positive ? "#22c55e" : "#ef4444",
          fontWeight: "bold",
          marginTop: "8px",
        }}
      >
        {change == null
          ? "--"
          : `${positive ? "▲" : "▼"} ${change.toFixed(
              2
            )} (${changePercent?.toFixed(2)}%)`}
      </p>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(2,1fr)",
          gap: "12px",
          marginTop: "24px",
        }}
      >
        <MetricCard
          title="HIGH"
          value={high.toFixed(2)}
        />

        <MetricCard
          title="LOW"
          value={low.toFixed(2)}
        />

        <MetricCard
          title="OPEN"
          value={open.toFixed(2)}
        />

        <MetricCard
          title="SOURCE"
          value={source}
        />
      </div>
    </div>
  );
}