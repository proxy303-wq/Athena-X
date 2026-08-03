type Props = {
  direction: string;
  confidence: number;
  trend: string;
  risk: string;
};

export default function DecisionCard({
  direction,
  confidence,
  trend,
  risk,
}: Props) {
  return (
    <div
      style={{
        marginTop: "40px",
        background: "#1e293b",
        borderRadius: "16px",
        padding: "24px",
        width: "100%",
      }}
    >
      <h2
        style={{
          fontSize: "24px",
          marginBottom: "20px",
        }}
      >
        AI Decision
      </h2>

      <h1
        style={{
          color: "#22c55e",
          fontSize: "30px",
          marginBottom: "20px",
        }}
      >
        {direction}
      </h1>

      <p>Confidence : {confidence}%</p>

      <p>Trend : {trend}</p>

      <p>Risk : {risk}</p>
    </div>
  );
}