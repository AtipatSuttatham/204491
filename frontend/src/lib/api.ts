import axios from 'axios'

/**
 * axios instance กลางของแอป — แนบ JWT access token อัตโนมัติ
 * (endpoint auth / interceptor สำหรับ refresh token จะเพิ่มตอน slice Authentication)
 */
export const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000/api',
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})
