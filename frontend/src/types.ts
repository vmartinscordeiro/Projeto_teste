export type Producer = { id: number; cpf_cnpj: string; name: string };
export type ProducerCreate = Omit<Producer, "id">;

export type Farm = {
  id: number;
  producer_id: number;
  name: string;
  city?: string | null;
  state?: string | null;
  area_total: number | string;
  area_agricultavel: number | string;
  area_vegetacao: number | string;
};
export type FarmCreate = Omit<Farm, "id">;

export type FarmCrop = { id: number; farm_id: number; season: string; crop: string };

export type DashboardSummary = { total_farms: number; total_hectares: number };
export type PieItem = { label: string; value: number };
