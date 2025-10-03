import { api } from "../lib/api";
import type { DashboardSummary, PieItem } from "../types";

export async function getSummary() {
  const { data } = await api.get<DashboardSummary>("/dashboard/summary");
  return data;
}
export async function getPieByState() {
  const { data } = await api.get<PieItem[]>("/dashboard/pie/state");
  return data;
}
export async function getPieByCrop() {
  const { data } = await api.get<PieItem[]>("/dashboard/pie/crop");
  return data;
}
export async function getPieLanduse() {
  const { data } = await api.get<PieItem[]>("/dashboard/pie/landuse");
  return data;
}
