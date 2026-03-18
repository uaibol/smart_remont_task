import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCartStore = defineStore('cart', () => {
  const items = ref([])

  const addToCart = (product) => {
    const existing = items.value.find(item => item.id === product.id)
    if (existing) {
      existing.qty += 1
    } else {
      items.value.push({ ...product, qty: 1 })
    }
  }

  const removeFromCart = (productId) => {
    items.value = items.value.filter(item => item.id !== productId)
  }

  const totalItems = computed(() => items.value.reduce((sum, item) => sum + item.qty, 0))

  const totalPrice = computed(() => items.value.reduce((sum, item) => sum + item.qty * parseFloat(item.price), 0))

  return { items, addToCart, removeFromCart, totalItems, totalPrice }
})