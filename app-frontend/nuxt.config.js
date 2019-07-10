export default {
  mode: 'universal',
  /*
   ** Headers of the page
   */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: { color: '#fff' },
  /*
   ** Global CSS
   */
  css: ['~/assets/css/tailwind.css', '~/assets/css/page-transitions.css'],
  /*
   ** Plugins to load before mounting the App
   */
  // CUSTOM: I create an env variable so that I can make a baseURL for my axios calls, see more: https://nuxtjs.org/api/configuration-env/
  env: {
    apiBaseUrl: process.env.BASE_URL || 'http://localhost:8000/api/'
  },
  plugins: [],
  /*
   ** Nuxt.js modules
   */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/pwa'
  ],
  /*
   ** Build configuration
   */
  buildDir: 'nuxt',
  build: {
    postcss: {
      plugins: {
        tailwindcss: './tailwind.config.js'
      }
    },
    // publicPath: '/assets/',
    extractCSS: true,
    babel: {
      presets: ({ isServer }) => [
        [
          '@nuxt/babel-preset-app',
          {
            targets: isServer ? { node: '8.11.1' } : { browsers: ['defaults'] }
          }
        ]
      ]
    },
    extend(config, ctx) {
      if (ctx.isDev && ctx.isClient) {
      }
    }
  }
}
