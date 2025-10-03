import { createGlobalStyle } from "styled-components";

export const GlobalStyle = createGlobalStyle`
  :root { color-scheme: dark; }

  *, *::before, *::after { box-sizing: border-box; }
  html, body, #root { height: 100%; }
  body {
    margin: 0;
    background: ${({ theme }) => theme.colors.bg};
    color: ${({ theme }) => theme.colors.text};
    font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, "Helvetica Neue", Arial, "Noto Sans";
    line-height: 1.45;
  }

  a { color: ${({ theme }) => theme.colors.primary}; text-decoration: none; }
  a:hover { color: ${({ theme }) => theme.colors.primaryHover}; }

  /* utilitários */
  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: ${({ theme }) => theme.spacing(6)};
  }

  .card {
    background: ${({ theme }) => theme.colors.surface};
    border: 1px solid ${({ theme }) => theme.colors.border};
    border-radius: 10px;
    padding: ${({ theme }) => theme.spacing(4)};
    box-shadow: ${({ theme }) => theme.shadow.sm};
  }

  /* layout responsivo para bordas */
  .screen {
    max-width: 1280px;
    margin: 0 auto;
    padding-inline: clamp(16px, 4vw, 40px);
  }

  main.screen { padding-block: 24px 48px; }
  header.screen { padding-block: 12px; }
`;
