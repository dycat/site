
const colors = require('tailwindcss/colors')

module.exports = {
  content: ['./templates/*.html'],
  theme: {
    extend: {
      colors: {
        green: colors.emerald,
        yellow: colors.amber,
        purple: colors.violet,
        gray: colors.neutral,
      }
    },
  },
  plugins: [require('@tailwindcss/typography'),],
}
