import { api } from "./api";
import type { Producer } from "../types";

export async function listProducers(): Promise<Producer[]> {
  const { data } = await api.get<Producer[]>("/producers");
  return data;
}
