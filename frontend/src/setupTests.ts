import "@testing-library/jest-dom";
import "whatwg-fetch";

// Polyfill básico para o ResponsiveContainer do Recharts
class ResizeObserver {
  observe() {}
  unobserve() {}
  disconnect() {}
}
(globalThis as any).ResizeObserver = (globalThis as any).ResizeObserver || ResizeObserver;

// Alguns gráficos/SVGs usam getBBox; no JSDOM não existe
// Stub simples para evitar erros de render
if (!(SVGElement as any).prototype.getBBox) {
  (SVGElement as any).prototype.getBBox = () => ({ x:0, y:0, width:0, height:0 });
}
