import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        ember: "#D6452A",
        sand: "#F4EBD0",
        ink: "#101820",
        mint: "#55D6BE",
      },
      fontFamily: {
        display: ["Sora", "Segoe UI", "sans-serif"],
        body: ["Manrope", "Segoe UI", "sans-serif"],
      },
      boxShadow: {
        glow: "0 0 40px rgba(214, 69, 42, 0.35)",
      },
      backgroundImage: {
        "hero-radial": "radial-gradient(circle at 20% 10%, rgba(214,69,42,0.35) 0%, rgba(16,24,32,0) 45%), radial-gradient(circle at 80% 20%, rgba(85,214,190,0.25) 0%, rgba(16,24,32,0) 40%)",
      },
      keyframes: {
        rise: {
          "0%": { opacity: "0", transform: "translateY(16px)" },
          "100%": { opacity: "1", transform: "translateY(0)" },
        },
      },
      animation: {
        rise: "rise 700ms ease-out both",
      },
    },
  },
  plugins: [],
};

export default config;
