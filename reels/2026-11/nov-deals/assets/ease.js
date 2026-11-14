// Shared timing helpers: everything is a pure function of t.
export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const prog = (t, a, b) => clamp((t - a) / (b - a));
export const outCubic = (x) => 1 - Math.pow(1 - x, 3);
export const outBack = (x, s = 1.9) => 1 + (s + 1) * Math.pow(x - 1, 3) + s * Math.pow(x - 1, 2);
export const inCubic = (x) => x * x * x;
export const fontsReady = () => document.fonts.ready;
export const tapeText = (txt, n = 14) => (txt + '  ✦  ').repeat(n);
