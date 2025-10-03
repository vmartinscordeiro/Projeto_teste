import { api } from "./api";
import type { Farm } from "../types";

type ListParams = { producer_id?: number };

export async function listFarms(params?: ListParams): Promise<Farm[]> {
  const { data } = await api.get<Farm[]>("/farms", { params });
  return data;
}

export async function createFarm(payload: Omit<Farm,"id">): Promise<Farm> {
  const { data } = await api.post<Farm>("/farms", payload);
  return data;
}
