import axios from "axios";

export const API_BASE =
  import.meta.env.VITE_API_BASE ?? "http://127.0.0.1:8000";

export const api = axios.create({
  baseURL: API_BASE,
  headers: { "Content-Type": "application/json" },
});
