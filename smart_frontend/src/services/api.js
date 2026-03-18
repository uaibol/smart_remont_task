import axios from 'axios'

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
  timeout: 5000
})

export const fetchProducts = () => api.get('products/')
export const fetchProductById = (id) => api.get(`products/${id}/`)

export default api