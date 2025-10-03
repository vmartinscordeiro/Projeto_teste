import { describe, it, expect, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import Dashboard from "../pages/Dashboard";

// mock dos serviços chamados pelo Dashboard
vi.mock("../services/dashboard", () => ({
  getSummary: () => Promise.resolve({ total_farms: 2, total_hectares: 2000 }),
  getPieByState: () => Promise.resolve([{ label: "MT", value: 2 }]),
  getPieByCrop: () => Promise.resolve([{ label: "Soja", value: 1 }, { label: "Milho", value: 1 }]),
  getPieLanduse: () => Promise.resolve([{ label: "Agricultável", value: 1400 }, { label: "Vegetação", value: 600 }]),
}));

describe("Dashboard page", () => {
  it("renderiza cards e títulos dos gráficos com dados mockados", async () => {
    render(<Dashboard />);

    // título da página
    expect(await screen.findByText(/Dashboard/i)).toBeInTheDocument();

    // cards
    await waitFor(() => {
      expect(screen.getByText(/Total de Fazendas/i)).toBeInTheDocument();
      expect(screen.getByText("2")).toBeInTheDocument();
      expect(screen.getByText(/Hectares \(total\)/i)).toBeInTheDocument();
      // aceita 2000, 2.000 ou 2,000
      expect(screen.getByText(/^(?:2000|2[.,]000)$/)).toBeInTheDocument();
    });

    // títulos dos gráficos
    expect(screen.getByText(/Fazendas por UF/i)).toBeInTheDocument();
    expect(screen.getByText(/Fazendas por Cultura/i)).toBeInTheDocument();
    expect(screen.getByText(/Uso do Solo \(ha\)/i)).toBeInTheDocument();
  });
});
