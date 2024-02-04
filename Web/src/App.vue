<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
<div class="bg-gray-300">
  <!-- Header -->
  <header class="bg-red-600 text-white p-3"> <!-- Se ajustó el color de fondo a rojo -->
    <div class="flex items-center justify-between">
      <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="50" height="50" />

      <nav class="space-x-4">
        <RouterLink to="/" class="hover:text-primary">Home</RouterLink>
        <RouterLink to="/about" class="hover:text-primary">About</RouterLink>
        <RouterLink to="/login" class="hover:text-primary">Login</RouterLink>
        <RouterLink to="/register" class="hover:text-primary">Registrar</RouterLink>
      </nav>
    </div>
  </header>

  <!-- Body -->
  <div class="flex-1 p-4 overflow-y-auto">
    <!-- RouterView que abarca toda la ventana sin padding -->
    <RouterView class="" />
  </div>
</div>

</template>



<style scoped>

</style>
