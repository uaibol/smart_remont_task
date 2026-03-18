<template>
  <div class="min-h-screen bg-gray-100">
    
    <header class="bg-white shadow p-4 flex justify-between items-center">
      <h1 class="font-bold text-xl">Smart Shop</h1>
      <router-link to="/" class="text-blue-500 hover:underline">Home</router-link>
      
    </header>
    <main class="p-4">
      <router-view></router-view>
    </main>
  </div>
</template>

<script setup>
</script>