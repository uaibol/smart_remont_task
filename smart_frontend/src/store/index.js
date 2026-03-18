import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useCartStore = defineStore('cart', () => {
  const cartItems = ref([])

  const addToCart = (product) => {
    const item = cartItems.value.find(i => i.id === product.id)
    if (item) {
      item.qty += 1
    } else {
      cartItems.value.push({ ...product, qty: 1 })
    }
    saveCart()
  }

  const removeFromCart = (id) => {
    cartItems.value = cartItems.value.filter(i => i.id !== id)
    saveCart()
  }

  const clearCart = () => {
    cartItems.value = []
    saveCart()
  }

  const saveCart = () => {
    localStorage.setItem('cart', JSON.stringify(cartItems.value))
  }

  const loadCart = () => {
    const data = localStorage.getItem('cart')
    if (data) cartItems.value = JSON.parse(data)
  }

  loadCart()

  return { cartItems, addToCart, removeFromCart, clearCart }
})