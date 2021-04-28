export const zeros = (w, h, v = 0) =>
  Array.from(new Array(h), (_) => Array(w).fill(v));
