import { Link, Route, Routes, NavLink } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import Producers from "./pages/Producers";

export default function App() {
  const linkStyle: React.CSSProperties = { padding: 8, textDecoration: "none" };
  const active: React.CSSProperties = { fontWeight: 700, textDecoration: "underline" };

  return (
    <div style={{ maxWidth: 1200, margin: "0 auto", padding: 16, display: "grid", gap: 16 }}>
      <header style={{ display: "flex", gap: 12 }}>
        <NavLink to="/" style={({ isActive }) => ({ ...linkStyle, ...(isActive ? active : {}) })}>
          Dashboard
        </NavLink>
        <NavLink to="/producers" style={({ isActive }) => ({ ...linkStyle, ...(isActive ? active : {}) })}>
          Produtores
        </NavLink>
      </header>

      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/producers" element={<Producers />} />
      </Routes>
    </div>
  );
}
