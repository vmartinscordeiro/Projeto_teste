// ERRADO (quebra em runtime):
// import { useDispatch, useSelector, TypedUseSelectorHook } from 'react-redux';

// CERTO (TypedUseSelectorHook é TIPO):
import { useDispatch, useSelector } from 'react-redux';
import type { TypedUseSelectorHook } from 'react-redux';

import type { RootState, AppDispatch } from './store'; // ajuste o caminho se for diferente

export const useAppDispatch: () => AppDispatch = useDispatch;
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;
