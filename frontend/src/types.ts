export type Producer = {
  id: number;
  cpf_cnpj: string;
  name: string;
};

export type Farm = {
  id: number;
  producer_id: number;
  name: string;
  city?: string | null;
  state?: string | null;            // UF
  area_total: number;
  area_agricultavel: number;
  area_vegetacao: number;
};

export type DashboardSummary = {
  total_farms: number;
  total_hectares: number;
};

export type PieItem = {
  name: string;
  value: number;
};
