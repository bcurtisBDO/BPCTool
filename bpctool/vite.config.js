import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

const adoProxy = {
  '/ado-proxy': {
    target: 'https://dev.azure.com',
    changeOrigin: true,
    secure: true,
    rewrite: (path) => path.replace(/^\/ado-proxy/, ''),
  },
  '/api': {
    target: 'http://127.0.0.1:8787',
    changeOrigin: true,
    rewrite: (path) => path.replace(/^\/api/, ''),
  },
}

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: adoProxy,
  },
  preview: {
    proxy: adoProxy,
  },
  test: {
    environment: 'node',
    include: ['src/**/*.test.js'],
  },
})
