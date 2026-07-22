import { defineConfig, globalIgnores } from "eslint/config"
import nextCoreWebVitals from "eslint-config-next/core-web-vitals"
import nextTypeScript from "eslint-config-next/typescript"

export default defineConfig([
  ...nextCoreWebVitals,
  ...nextTypeScript,
  {
    files: ["**/*.{ts,tsx}"],
    languageOptions: {
      parserOptions: {
        projectService: true,
        tsconfigRootDir: import.meta.dirname,
      },
    },
    rules: {
      "@next/next/no-html-link-for-pages": "error",
      "@typescript-eslint/no-floating-promises": "error",
      "import/order": [
        "error",
        {
          alphabetize: { caseInsensitive: true, order: "asc" },
          "newlines-between": "always",
        },
      ],
    },
  },
  globalIgnores([
    ".artifacts/bootstrap/**",
    ".next/**",
    "build/**",
    "coverage/**",
    "next-env.d.ts",
    "out/**",
  ]),
])
