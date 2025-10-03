import { api } from "../lib/api";
import type { Producer, ProducerCreate } from "../types";

export async function listProducers() {
  const { data } = await api.get<Producer[]>("/producers");
  return data;
}
export async function createProducer(payload: ProducerCreate) {
  const { data } = await api.post<Producer>("/producers", payload);
  return data;
}
export async function deleteProducer(id: number) {
  await api.delete(`/producers/${id}`);
}
