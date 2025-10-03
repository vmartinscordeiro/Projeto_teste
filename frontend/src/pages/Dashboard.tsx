import { useEffect, useState } from "react";
import {
  getSummary,
  getPieByState,
  getPieByCrop,
  getPieLanduse,
} from "../services/dashboard";
import type { DashboardSummary, PieItem } from "../types";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

export default function Dashboard() {
  const [summary, setSummary] = useState<DashboardSummary | null>(null);
  const [byState, setByState] = useState<PieItem[]>([]);
  const [byCrop, setByCrop] = useState<PieItem[]>([]);
  const [land, setLand] = useState<PieItem[]>([]);

  useEffect(() => {
    (async () => {
      setSummary(await getSummary());
      setByState(await getPieByState());
      setByCrop(await getPieByCrop());
      setLand(await getPieLanduse());
    })();
  }, []);

  return (
    <div style={{ display: "grid", gap: 16 }}>
      <h2>Dashboard</h2>

      {summary && (
        <div style={{ display: "flex", gap: 16, flexWrap: "wrap" }}>
          <StatCard label="Total de Fazendas" value={summary.total_farms} />
          <StatCard
            label="Hectares (total)"
            value={summary.total_hectares}
            format="number"
          />
        </div>
      )}

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(3, minmax(280px, 1fr))",
          gap: 16,
        }}
      >
        <Chart title="Fazendas por UF" data={byState} />
        <Chart title="Fazendas por Cultura" data={byCrop} />
        <Chart title="Uso do Solo (ha)" data={land} />
      </div>
    </div>
  );
}

function StatCard({
  label,
  value,
  format,
}: {
  label: string;
  value: number;
  format?: "number";
}) {
  const shown =
    format === "number"
      ? Number(value).toLocaleString("pt-BR")
      : value.toLocaleString("pt-BR");

  return (
    <div
      style={{
        padding: 12,
        border: "1px solid #333",
        borderRadius: 8,
        minWidth: 220,
      }}
    >
      <div style={{ opacity: 0.8 }}>{label}</div>
      <b style={{ fontSize: 28 }}>{shown}</b>
    </div>
  );
}

function Chart({ title, data }: { title: string; data: PieItem[] }) {
  const colors = ["#8884d8", "#82ca9d", "#ffc658", "#ff8042", "#8dd1e1", "#a4de6c"];

  return (
    <div
      style={{
        height: 340,
        border: "1px solid #333",
        borderRadius: 8,
        padding: 8,
      }}
    >
      <h4 style={{ margin: 0, marginBottom: 8 }}>{title}</h4>

      {!data?.length ? (
        <div
          style={{
            height: "90%",
            display: "grid",
            placeItems: "center",
            opacity: 0.7,
          }}
        >
          Sem dados
        </div>
      ) : (
        <div style={{ width: "100%", height: "90%" }}>
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie data={data} dataKey="value" nameKey="label" outerRadius={110} label>
                {data.map((_, i) => (
                  <Cell key={`${title}-${i}`} fill={colors[i % colors.length]} />
                ))}
              </Pie>
              <Tooltip />
              <Legend />
            </PieChart>
          </ResponsiveContainer>
        </div>
      )}
    </div>
  );
}
