/** @type {import('tailwindcss').Config} */
export default {
  // Tell Tailwind where to scan for class names
  content: [
    "./src/**/*.{astro,html,md,mdx,ts,tsx,js,jsx}",
  ],

  // We’ll control dark mode manually by toggling a 'dark' class on <html>
  darkMode: "class",

  theme: {
    extend: {
      // Your premium dark palette (adjust if you like)
      colors: {
        bg: "#0C1117",       // page background
        surface: "#0F1722",  // cards / surfaces
        text: "#D4D9E3",     // primary text
        muted: "#98A1B3",    // secondary text
        accent: "#22D3EE"    // links / highlights (cyan)
      },

      // Optional: a nicer container helper
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

      // Optional: typography tweaks for long-form MDX
      typography: {
        DEFAULT: {
          css: {
            color: "#D4D9E3",
            a: { color: "#22D3EE", textDecoration: "none" },
            strong: { color: "#E6EBF5" },
            code: { color: "#E6EBF5" },
            blockquote: { color: "#C7CEDD", borderLeftColor: "rgba(255,255,255,0.1)" },
          },
        },
        invert: {
          css: {
            color: "#D4D9E3",
            a: { color: "#22D3EE" },
            strong: { color: "#E6EBF5" },
            code: { color: "#E6EBF5" },
            blockquote: { color: "#C7CEDD", borderLeftColor: "rgba(255,255,255,0.1)" },
          },
        },
      },
    },
  },

  // Enable official plugins
  plugins: [
    require("@tailwindcss/typography"),
  ],
};
