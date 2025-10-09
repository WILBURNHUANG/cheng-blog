/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./src/**/*.{astro,html,md,mdx,ts,tsx,js,jsx}",
  ],
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        bg: "#050A19",
        surface: "#0A1530",
        surfaceMuted: "#0F1D3D",
        text: "#F1F5FF",
        muted: "#9DB4D8",
        accent: "#5CE1FF",
      },
      fontFamily: {
        sans: ["'Inter'", "'Space Grotesk'", "system-ui", "-apple-system", "BlinkMacSystemFont", "'Segoe UI'", "sans-serif"],
        display: ["'Space Grotesk'", "'Inter'", "system-ui", "sans-serif"],
      },
      container: {
        center: true,
        padding: "1rem",
        screens: {
          sm: "640px",
          md: "768px",
          lg: "1024px",
          xl: "1280px",
          "2xl": "1400px",
        },
      },
      typography: {
        DEFAULT: {
          css: {
            color: "#E6EEFF",
            a: { color: "#5CE1FF", textDecoration: "none" },
            strong: { color: "#F7FAFF" },
            code: { color: "#F7FAFF" },
            blockquote: {
              color: "#D0E0FF",
              borderLeftColor: "rgba(92,225,255,0.3)",
              backgroundColor: "rgba(10,21,48,0.6)",
            },
          },
        },
        invert: {
          css: {
            color: "#E6EEFF",
            a: { color: "#5CE1FF" },
            strong: { color: "#F7FAFF" },
            code: { color: "#F7FAFF" },
            blockquote: {
              color: "#D0E0FF",
              borderLeftColor: "rgba(92,225,255,0.3)",
              backgroundColor: "rgba(10,21,48,0.6)",
            },
          },
        },
      },
    },
  },
  plugins: [
    require("@tailwindcss/typography"),
  ],
};
