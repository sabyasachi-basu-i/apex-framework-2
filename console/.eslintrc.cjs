module.exports = {
  root: true,
  extends: ['next/core-web-vitals', 'eslint-config-prettier'],
  rules: {
    // TypeScript's type system already flags undefined identifiers,
    // so this rule can incorrectly warn on type-only globals like RequestInit.
    'no-undef': 'off',
  },
};
