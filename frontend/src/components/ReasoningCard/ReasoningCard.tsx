type Props = {
  reasoning: string[];
  direction: string;
  confidence: number;
};

export default function ReasoningCard({
  reasoning,
  direction,
  confidence,
}: Props) {
  return (
    <div
      style={{
        background: "#1e293b",
        borderRadius: "18px",
        padding: "28px",
        boxShadow: "0 10px 30px rgba(0,0,0,.25)",
      }}
    >
      <h2
        style={{
          marginBottom: "24px",
          fontSize: "24px",
        }}
      >
        🧠 Athena AI
      </h2>

      {reasoning.map((reason, index) => (
        <div
          key={index}
          style={{
            display: "flex",
            alignItems: "center",
            marginBottom: "14px",
            color: "#f8fafc",
          }}
        >
          <span
            style={{
              color: reason.includes("Overbought")
                ? "#f59e0b"
                : "#22c55e",
              marginRight: "12px",
              fontWeight: 700,
            }}
          >
            {reason.includes("Overbought") ? "⚠" : "✓"}
          </span>

          {reason}
        </div>
      ))}

      <hr
        style={{
          margin: "24px 0",
          borderColor: "#334155",
        }}
      />

      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
        }}
      >
        <div>
          <div
            style={{
              color: "#94a3b8",
              fontSize: "14px",
            }}
          >
            SIGNAL
          </div>

          <div
            style={{
              fontSize: "28px",
              fontWeight: 700,
              color: "#22c55e",
            }}
          >
            {direction}
          </div>
        </div>

        <div
          style={{
            textAlign: "right",
          }}
        >
          <div
            style={{
              color: "#94a3b8",
              fontSize: "14px",
            }}
          >
            CONFIDENCE
          </div>

          <div
            style={{
              fontSize: "34px",
              fontWeight: 700,
            }}
          >
            {confidence}%
          </div>
        </div>
      </div>
    </div>
  );
}