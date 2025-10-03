import { useEffect, useMemo, useState } from "react";
import { listProducers } from "../services/producers";
import { createFarm, listFarms } from "../services/farms";
import type { Producer, Farm } from "../types";

function toNum(x: number | string) { return typeof x === "number" ? x : Number(x); }

export default function Farms() {
  const [producers, setProducers] = useState<Producer[]>([]);
  const [farms, setFarms] = useState<Farm[]>([]);
  const [producerId, setProducerId] = useState<number | "">("");
  const [name, setName] = useState("");
  const [city, setCity] = useState("");
  const [state, setState] = useState("");
  const [areaT, setAreaT] = useState("0");
  const [areaA, setAreaA] = useState("0");
  const [areaV, setAreaV] = useState("0");
  const [msg, setMsg] = useState<string | null>(null);

  async function refreshList() {
    setFarms(await listFarms(typeof producerId === "number" ? { producer_id: producerId } : undefined));
  }

  useEffect(() => {
    (async () => {
      const ps = await listProducers();
      setProducers(ps);
      await refreshList();
    })();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => { refreshList(); }, [producerId]); // filtra por produtor

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setMsg(null);
    if (producerId === "") { setMsg("Selecione um produtor."); return; }
    try {
      await createFarm({
        producer_id: producerId,
        name, city, state,
        area_total: Number(areaT),
        area_agricultavel: Number(areaA),
        area_vegetacao: Number(areaV),
      } as any);
      setName(""); setCity(""); setState(""); setAreaT("0"); setAreaA("0"); setAreaV("0");
      await refreshList();
    } catch (err:any) {
      setMsg(err?.response?.data?.detail ?? "Erro ao criar fazenda.");
    }
  }

  return (
    <div style={{display:"grid", gap:16}}>
      <h2>Fazendas</h2>

      <div style={{display:"flex", gap:8, alignItems:"center"}}>
        <label>Filtrar por produtor:</label>
        <select value={producerId} onChange={e=>setProducerId(e.target.value === "" ? "" : Number(e.target.value))}>
          <option value="">(Todos)</option>
          {producers.map(p => <option key={p.id} value={p.id}>{p.id} - {p.name}</option>)}
        </select>
      </div>

      <form onSubmit={onSubmit} style={{display:"grid", gridTemplateColumns:"repeat(4, 1fr)", gap:8}}>
        <select required value={producerId} onChange={e=>setProducerId(Number(e.target.value))}>
          <option value="">Selecione o produtor…</option>
          {producers.map(p => <option key={p.id} value={p.id}>{p.id} - {p.name}</option>)}
        </select>
        <input placeholder="Nome" value={name} onChange={e=>setName(e.target.value)} />
        <input placeholder="Cidade" value={city} onChange={e=>setCity(e.target.value)} />
        <input placeholder="UF" maxLength={2} value={state} onChange={e=>setState(e.target.value.toUpperCase())} />
        <input placeholder="Área total (ha)" value={areaT} onChange={e=>setAreaT(e.target.value)} />
        <input placeholder="Agricultável (ha)" value={areaA} onChange={e=>setAreaA(e.target.value)} />
        <input placeholder="Vegetação (ha)" value={areaV} onChange={e=>setAreaV(e.target.value)} />
        <button type="submit">Adicionar fazenda</button>
        {msg && <span style={{gridColumn:"1 / -1", color:"#f55"}}>{String(msg)}</span>}
      </form>

      <table>
        <thead><tr><th>ID</th><th>Produtor</th><th>Nome</th><th>Cidade</th><th>UF</th><th>Área</th></tr></thead>
        <tbody>
          {farms.map(f=>(
            <tr key={f.id}>
              <td>{f.id}</td>
              <td>{f.producer_id}</td>
              <td>{f.name}</td>
              <td>{f.city ?? "-"}</td>
              <td>{f.state ?? "-"}</td>
              <td>
                T {toNum(f.area_total)} / Agri {toNum(f.area_agricultavel)} / Veg {toNum(f.area_vegetacao)}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
