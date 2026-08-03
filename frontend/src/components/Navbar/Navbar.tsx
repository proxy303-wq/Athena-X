export default function Navbar() {
  return (
    <nav
      style={{
        height: "70px",
        background: "#111827",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "0 30px",
        borderBottom: "1px solid #1f2937",
      }}
    >
      <div>
        <h2>Athena X</h2>
      </div>

      <div
        style={{
          display: "flex",
          alignItems: "center",
          gap: "20px",
        }}
      >
        <span
          style={{
            color: "#22c55e",
            fontWeight: "bold",
          }}
        >
          ● LIVE
        </span>

        <span>NIFTY</span>
      </div>
    </nav>
  );
}