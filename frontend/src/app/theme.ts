import { extendTheme } from "@chakra-ui/react";

export const theme = extendTheme({
  colors: {
    brand: {
      50: "#e6f0ff",
      100: "#b3d1ff",
      200: "#80b2ff",
      300: "#4d94ff",
      400: "#1a75ff",
      500: "#0062ff",
      600: "#004dcf",
      700: "#003799",
      800: "#002266",
      900: "#000d33",
    },
  },
  fonts: {
    heading: "Inter, sans-serif",
    body: "Inter, sans-serif",
  },
});
