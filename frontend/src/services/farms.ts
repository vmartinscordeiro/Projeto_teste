import { api } from "../lib/api";
import type { Farm, FarmCreate } from "../types";

export async function listFarms(params?: { producer_id?: number }) {
  const { data } = await api.get<Farm[]>("/farms", { params });
  return data;
}
export async function createFarm(payload: FarmCreate) {
  const { data } = await api.post<Farm>("/farms", payload);
  return data;
}
