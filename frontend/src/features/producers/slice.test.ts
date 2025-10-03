import reducer, { setProducers, addProducer, type Producer } from "./slice";

describe("producers slice", () => {
  it("deve setar a lista de producers", () => {
    const initial = { items: [], status: "idle" as const };
    const payload: Producer[] = [
      { id: 1, cpf_cnpj: "52998224725", name: "João" },
      { id: 2, cpf_cnpj: "39053344705", name: "Maria" },
    ];
    const next = reducer(initial, setProducers(payload));
    expect(next.items).toHaveLength(2);
    expect(next.items[0].name).toBe("João");
  });

  it("deve adicionar um producer", () => {
    const initial = { items: [], status: "idle" as const };
    const novo: Producer = { id: 3, cpf_cnpj: "01234567890", name: "Novo" };
    const next = reducer(initial, addProducer(novo));
    expect(next.items).toHaveLength(1);
    expect(next.items[0].id).toBe(3);
  });
});
