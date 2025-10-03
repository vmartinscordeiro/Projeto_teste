import { useEffect, useState } from "react";
import { useAppDispatch, useAppSelector } from "../hooks";
import { fetchProducers, createProducer } from "../features/producers/slice";

export default function Producers() {
  const dispatch = useAppDispatch();
  const { items, status } = useAppSelector((s) => s.producers);

  const [cpf, setCpf] = useState("");
  const [name, setName] = useState("");

  useEffect(() => {
    // carrega lista ao montar
    dispatch(fetchProducers());
  }, [dispatch]);

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!cpf || !name) return;
    await dispatch(createProducer({ cpf_cnpj: cpf, name }));
    setCpf("");
    setName("");
  };

  return (
    <div style={{ display: "grid", gap: 16 }}>
      <h2>Produtores</h2>

      <form onSubmit={onSubmit} style={{ display: "flex", gap: 12, flexWrap: "wrap" }}>
        <div style={{ display: "grid" }}>
          <label htmlFor="cpf">CPF/CNPJ</label>
          <input
            id="cpf"
            aria-label="CPF/CNPJ"
            value={cpf}
            onChange={(e) => setCpf(e.target.value)}
            placeholder="somente números"
          />
        </div>
        <div style={{ display: "grid" }}>
          <label htmlFor="name">Nome</label>
          <input
            id="name"
            aria-label="Nome"
            value={name}
            onChange={(e) => setName(e.target.value)}
            placeholder="Nome do produtor"
          />
        </div>
        <button type="submit" disabled={!cpf || !name || status === "loading"}>
          Adicionar
        </button>
      </form>

      <div style={{ borderTop: "1px solid #333", paddingTop: 8 }}>
        {status === "loading" && <div>Carregando...</div>}
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr>
              <th style={{ textAlign: "left", padding: 4 }}>ID</th>
              <th style={{ textAlign: "left", padding: 4 }}>CPF/CNPJ</th>
              <th style={{ textAlign: "left", padding: 4 }}>Nome</th>
            </tr>
          </thead>
          <tbody>
            {items.map((p) => (
              <tr key={p.id}>
                <td style={{ padding: 4 }}>{p.id}</td>
                <td style={{ padding: 4 }}>{p.cpf_cnpj}</td>
                <td style={{ padding: 4 }}>{p.name}</td>
              </tr>
            ))}
            {items.length === 0 && status !== "loading" && (
              <tr>
                <td colSpan={3} style={{ padding: 4, opacity: 0.7 }}>
                  Nenhum produtor.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}
