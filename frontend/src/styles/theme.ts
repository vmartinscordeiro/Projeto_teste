export const theme = {
  name: 'dark',
  colors: {
    bg: '#0f0f10',
    surface: '#16171a',
    border: '#23252a',
    text: '#e8e8ea',
    textMuted: '#b8b8bb',
    primary: '#a78bfa',
    primaryHover: '#c4b5fd',
    success: '#22c55e',
    danger: '#ef4444',
    warning: '#f59e0b',
  },
  radius: { sm: '8px', md: '12px', lg: '16px' },
  shadow: { sm: '0 1px 2px rgba(0,0,0,.25)', md: '0 6px 20px rgba(0,0,0,.35)' },
  spacing: (n: number) => `${n * 4}px`,
};
export type AppTheme = typeof theme;
