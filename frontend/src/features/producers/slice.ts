import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import type { PayloadAction } from "@reduxjs/toolkit";
import { api } from "../../services/api";

export type Producer = {
  id: number;
  cpf_cnpj: string;
  name: string;
};

type ProducersState = {
  items: Producer[];
  status: "idle" | "loading" | "succeeded" | "failed";
  error?: string;
};

const initialState: ProducersState = {
  items: [],
  status: "idle",
};

// Thunks (opcional – úteis p/ quando plugar na UI)
export const fetchProducers = createAsyncThunk<Producer[]>(
  "producers/fetch",
  async () => {
    const { data } = await api.get<Producer[]>("/producers");
    return data;
  }
);

export const createProducer = createAsyncThunk<
  Producer,
  { cpf_cnpj: string; name: string }
>("producers/create", async (payload) => {
  const { data } = await api.post<Producer>("/producers", payload);
  return data;
});

// Slice
const producersSlice = createSlice({
  name: "producers",
  initialState,
  reducers: {
    // Ações síncronas (fáceis de testar)
    setProducers(state, action: PayloadAction<Producer[]>) {
      state.items = action.payload;
    },
    addProducer(state, action: PayloadAction<Producer>) {
      state.items.push(action.payload);
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchProducers.pending, (state) => {
        state.status = "loading";
      })
      .addCase(fetchProducers.fulfilled, (state, action) => {
        state.status = "succeeded";
        state.items = action.payload;
      })
      .addCase(fetchProducers.rejected, (state, action) => {
        state.status = "failed";
        state.error = action.error?.message ?? "Erro ao carregar produtores";
      })
      .addCase(createProducer.fulfilled, (state, action) => {
        state.items.push(action.payload);
      });
  },
});

export const { setProducers, addProducer } = producersSlice.actions;
export default producersSlice.reducer;
