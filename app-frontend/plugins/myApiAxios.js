// CUSTOM: I create my own axios instance wit the base URL from nuxt.config env var.
// This way I can keep the HTTP URLS a bit more DRY.

import axios from 'axios'

export default axios.create({
  baseURL: process.env.apiBaseUrl
})
