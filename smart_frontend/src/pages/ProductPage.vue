<template>
  <div>
    <h2 class="text-2xl font-bold mb-4">{{ product?.name }}</h2>
    <img :src="product?.image" alt="" class="w-64 h-64 object-cover mb-4"/>
    <p class="text-gray-700">${{ product?.price }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { fetchProductById } from '../services/api'

const route = useRoute()
const product = ref(null)

onMounted(async () => {
  const res = await fetchProductById(route.params.id)
  product.value = res.data
})
</script>