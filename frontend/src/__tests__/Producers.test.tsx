import { describe, it, expect, vi } from "vitest";
import { render, screen, waitFor, fireEvent } from "@testing-library/react";
import { Provider } from "react-redux";
import { store } from "../store";
import Producers from "../pages/Producers";

// mock do cliente HTTP usado nos thunks
vi.mock("../services/api", () => {
  return {
    api: {
      get: vi.fn().mockResolvedValue({
        data: [{ id: 1, cpf_cnpj: "52998224725", name: "João" }],
      }),
      post: vi.fn().mockResolvedValue({
        data: { id: 2, cpf_cnpj: "01234567890", name: "Maria" },
      }),
    },
  };
});

function renderWithProviders(ui: React.ReactElement) {
  return render(<Provider store={store}>{ui}</Provider>);
}

describe("Producers page", () => {
  it("lista e permite adicionar produtor (mockado)", async () => {
    renderWithProviders(<Producers />);

    // título
    expect(await screen.findByText(/Produtores/i)).toBeInTheDocument();

    // lista inicial mockada
    await waitFor(() => {
      expect(screen.getByText("João")).toBeInTheDocument();
    });

    // preencher formulário e enviar
    fireEvent.change(screen.getByLabelText(/CPF\/CNPJ/i), {
      target: { value: "01234567890" },
    });
    fireEvent.change(screen.getByLabelText(/Nome/i), {
      target: { value: "Maria" },
    });
    fireEvent.click(screen.getByRole("button", { name: /Adicionar/i }));

    // novo item aparece
    await waitFor(() => {
      expect(screen.getByText("Maria")).toBeInTheDocument();
    });
  });
});
