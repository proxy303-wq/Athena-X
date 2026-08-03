import { useEffect, useState } from "react";

import api from "./services/api";

import MainLayout from "./layouts/MainLayout";
import Dashboard from "./pages/Dashboard/Dashboard";

import type { DashboardResponse } from "./types/dashboard";

function App() {
  const [dashboard, setDashboard] =
    useState<DashboardResponse | null>(null);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  const loadDashboard = async () => {
    try {
      const res = await api.get("/dashboard/NIFTY");

      setDashboard(res.data);

      setError("");
    } catch (err) {
      console.error(err);

      setError("Unable to connect to Athena Backend.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadDashboard();

    const interval = setInterval(() => {
      loadDashboard();
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  if (loading) {
    return (
      <div
        style={{
          minHeight: "100vh",
          background: "#0f172a",
          color: "white",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          fontSize: 24,
        }}
      >
        🚀 Loading Athena X...
      </div>
    );
  }

  if (error !== "") {
    return (
      <div
        style={{
          minHeight: "100vh",
          background: "#0f172a",
          color: "#ef4444",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          fontSize: 24,
        }}
      >
        {error}
      </div>
    );
  }

  return (
    <MainLayout>
      {dashboard && <Dashboard dashboard={dashboard} />}
    </MainLayout>
  );
}

export default App;