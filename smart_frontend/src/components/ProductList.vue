<template>
  <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
    <ProductCard
      v-for="product in products"
      :key="product.id"
      :product="product"
      @select="$emit('select', $event)"
    />
  </div>
</template>

<script setup>
import ProductCard from './ProductCard.vue'
const props = defineProps({ products: Array })
</script>