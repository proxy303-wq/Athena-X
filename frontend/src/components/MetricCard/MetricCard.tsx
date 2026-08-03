type Props = {
  title: string;
  value: string | number;
};

export default function MetricCard({
  title,
  value,
}: Props) {
  return (
    <div
      style={{
        background: "#0f172a",
        border: "1px solid #334155",
        borderRadius: "12px",
        padding: "16px",
      }}
    >
      <div
        style={{
          fontSize: "12px",
          color: "#94a3b8",
          marginBottom: "8px",
        }}
      >
        {title}
      </div>

      <div
        style={{
          fontSize: "20px",
          fontWeight: "bold",
        }}
      >
        {value}
      </div>
    </div>
  );
}