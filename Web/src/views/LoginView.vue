<template>
	<div class="bg-gray-100 h-screen flex items-center justify-center">
	  <div class="bg-white p-8 rounded shadow-md w-full max-w-md">
		<h2 class="text-2xl font-semibold mb-6">Iniciar Sesión</h2>
  
		<form @submit.prevent="login">
		  <div class="mb-4">
			<label for="username" class="block text-gray-600 text-sm font-medium mb-2">Nombre de usuario</label>
			<input v-model="username" type="text" id="username" name="username" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500" placeholder="Ingresa tu nombre de usuario" required>
		  </div>
  
		  <div class="mb-4">
			<label for="password" class="block text-gray-600 text-sm font-medium mb-2">Contraseña</label>
			<input v-model="password" type="password" id="password" name="password" class="w-full px-4 py-2 border rounded-md focus:outline-none focus:border-blue-500" placeholder="Ingresa tu contraseña" required>
		  </div>
  
		  <button type="submit" class="w-full bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 transition duration-300">Iniciar Sesión</button>
		</form>
	  </div>
	</div>
  </template>
  
  <script>
  export default {
	data() {
	  return {
		username: '',
		password: '',
	  };
	},
	methods: {
	  login() {
		// Aquí puedes agregar la lógica de inicio de sesión
		console.log('Iniciar sesión con:', this.username, this.password);
	  },
	},
  };
  </script>
  
  <style>
  /* Agrega estilos adicionales según sea necesario */
  </style>
  