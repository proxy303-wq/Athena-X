import type { CSSProperties } from "react";

type Props = {
  callDelta: number;
  putDelta: number;
  gamma: number;
  theta: number;
  iv: number;
};

export default function GreeksCard({
  callDelta,
  putDelta,
  gamma,
  theta,
  iv,
}: Props) {
  const cardStyle: CSSProperties = {
    background: "#1e293b",
    borderRadius: "18px",
    padding: "28px",
    boxShadow: "0 10px 30px rgba(0,0,0,.25)",
  };

  const rowStyle: CSSProperties = {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: "18px",
  };

  const valueStyle: CSSProperties = {
    fontWeight: 700,
    color: "#f8fafc",
  };

  return (
    <div style={cardStyle}>
      <h2
        style={{
          marginBottom: "24px",
          fontSize: "24px",
          color: "#f8fafc",
        }}
      >
        Greeks
      </h2>

      <div style={rowStyle}>
        <span>Call Delta</span>
        <span style={valueStyle}>{callDelta.toFixed(4)}</span>
      </div>

      <div style={rowStyle}>
        <span>Put Delta</span>
        <span style={valueStyle}>{putDelta.toFixed(4)}</span>
      </div>

      <div style={rowStyle}>
        <span>Gamma</span>
        <span style={valueStyle}>{gamma.toFixed(4)}</span>
      </div>

      <div style={rowStyle}>
        <span>Theta</span>
        <span style={valueStyle}>{theta.toFixed(2)}</span>
      </div>

      <div style={rowStyle}>
        <span>Implied Volatility</span>
        <span
          style={{
            color: "#22c55e",
            fontWeight: 700,
          }}
        >
          {iv.toFixed(2)}%
        </span>
      </div>
    </div>
  );
}