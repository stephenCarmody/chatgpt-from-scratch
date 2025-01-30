import globals from "globals";
import pluginJs from "@eslint/js";
import pluginVue from "eslint-plugin-vue";


/** @type {import('eslint').Linter.Config[]} */
export default [
  {
    files: ["**/*.{js,mjs,cjs,vue}"],
    ignores: [
      "**/dist/*",
      "./node_modules/**/*",
      '**/dev/*',
      '**/tests/*',
    ]
  },
  {
    ...pluginJs.configs.recommended,
    ignores: ["dist/**/*.js"]
  },
  {files: ["**/*.js"], languageOptions: {sourceType: "commonjs"}},
  {languageOptions: { globals: globals.browser }},
  ...pluginVue.configs["flat/essential"],
];