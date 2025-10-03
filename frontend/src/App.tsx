import { Link, Route, Routes, Navigate } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import ProducersPage from "./pages/Producers";
import Farms from "./pages/Farms";

export default function App() {
  return (
    <div>
      <header className="screen">
        <nav style={{ display:"flex", gap:16, height:56, alignItems:"center" }}>
          <Link to="/" style={{ marginRight: 16 }}>Dashboard</Link>
          <Link to="/producers" style={{ marginRight: 16 }}>Produtores</Link>
          <Link to="/farms">Fazendas</Link>
        </nav>
      </header>

      <main className="screen">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/producers" element={<ProducersPage />} />
          <Route path="/farms" element={<Farms />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
    </div>
  );
}
