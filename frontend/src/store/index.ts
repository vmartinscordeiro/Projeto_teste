import { configureStore } from "@reduxjs/toolkit";
import producersReducer from "../features/producers/slice";

export const store = configureStore({
  reducer: {
    producers: producersReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
