<template>
  <div
    class="fixed right-4 top-4 w-80 p-4 border rounded bg-white shadow-lg"
    @dragover.prevent
    @drop="dropProduct"
  >
    <h2 class="font-bold text-xl mb-2">Себет</h2>
    <div v-if="cart.cartItems.length === 0" class="text-gray-500">Себет бос</div>
    <div v-for="item in cart.cartItems" :key="item.id" class="flex justify-between mb-2">
      <div>{{ item.name }} x {{ item.qty }}</div>
      <button @click="cart.removeFromCart(item.id)" class="text-red-500">✕</button>
    </div>
    <div class="mt-2 font-bold">
      Жалпы: {{ total }} ₸
    </div>
    <button @click="cart.clearCart" class="mt-2 w-full bg-red-500 text-white p-2 rounded hover:bg-red-600">
      Тазалау
    </button>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useCartStore } from '../store'

const cart = useCartStore()

const dropProduct = (event) => {
  const product = JSON.parse(event.dataTransfer.getData('product'))
  cart.addToCart(product)
}

const total = computed(() => cart.cartItems.reduce((sum, i) => sum + i.qty * parseFloat(i.price), 0))
</script>