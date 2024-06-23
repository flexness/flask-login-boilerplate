module.exports = {
  content: [
      "./app/templates/**/*.html",
      "./app/static/src/**/*.js",
      "./node_modules/flowbite/**/*.js",
      './app/static/src/custom.css'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("flowbite/plugin")
  ],
}
