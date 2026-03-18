<template>
  <div
    class="border rounded p-4 hover:shadow-lg transition relative cursor-grab"
    draggable="true"
    @dragstart="dragStart"
  >
    <img :src="product.image" class="w-full h-40 object-cover mb-2 rounded" />
    <h3 class="font-bold text-lg">{{ product.name }}</h3>
    <p class="text-gray-600 mb-8">{{ product.price }} ₸</p>

    <button
      @click="addToCart"
      class="absolute bottom-2 right-2 bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600 transition"
    >
      Себетке қосу
    </button>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
import { useCartStore } from '../store'

const props = defineProps({
  product: Object
})

const cart = useCartStore()

const dragStart = (event) => {
  event.dataTransfer.setData('product', JSON.stringify(props.product))
}

const addToCart = () => {
  cart.addToCart(props.product)
}
</script>