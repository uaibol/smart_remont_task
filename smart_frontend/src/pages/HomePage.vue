<template>
  <div class="p-6">
    <Cart />
    <h2 class="text-3xl font-bold mb-6">Өнімдер</h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
      <ProductCard
        v-for="product in products"
        :key="product.id"
        :product="product"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ProductCard from '../components/ProductCard.vue'
import Cart from '../components/Cart.vue'
import { fetchProducts } from '../services/api.js'

const products = ref([])

onMounted(async () => {
  try {
    const res = await fetchProducts()
    products.value = Array.isArray(res.data.results) ? res.data.results : []
  } catch (err) {
    console.error('Failed to fetch products', err)
    products.value = []
  }
})
</script>