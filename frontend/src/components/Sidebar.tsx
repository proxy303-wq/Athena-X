export default function Sidebar() {
  const menus = [
    "Dashboard",
    "Market",
    "Options",
    "Analytics",
    "History",
    "Settings",
  ];

  return (
    <aside
      style={{
        width: "230px",
        background: "#111827",
        padding: "25px",
        minHeight: "calc(100vh - 70px)",
      }}
    >
      {menus.map((menu) => (
        <div
          key={menu}
          style={{
            marginBottom: "22px",
            cursor: "pointer",
            fontSize: "17px",
          }}
        >
          {menu}
        </div>
      ))}
    </aside>
  );
}