import Navbar from "../components/Navbar/Navbar";
import Sidebar from "../components/Sidebar";

type Props = {
  children: React.ReactNode;
};

export default function MainLayout({ children }: Props) {
  return (
    <div
      style={{
        background: "#0f172a",
        minHeight: "100vh",
        color: "white",
      }}
    >
      <Navbar />

      <div
        style={{
          display: "flex",
        }}
      >
        <Sidebar />

        <main
          style={{
            flex: 1,
            padding: "32px",
          }}
        >
          {children}
        </main>
      </div>
    </div>
  );
}