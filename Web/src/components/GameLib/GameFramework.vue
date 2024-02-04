<template>
    <div ref="gameContainerRef"></div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';

  const { message, w, h } = defineProps(['message', 'w', 'h']);

  const gameContainerRef = ref(null);

  onMounted(() => {
    // Puedes usar las propiedades pasadas al componente aquí
    console.log(message, w, h);

    // Inicializar Crafty.js en el contenedor del juego al montar el componente
    Crafty.init(w, h, gameContainerRef.value);
    Crafty.background('#000000');
  
    // Crear una entidad con un rectángulo rojo que se mueve
    Crafty.e('2D, Canvas, Color, Twoway')
      .attr({ x: 10, y: 10, w: 50, h: 50 })
      .color('red')
      .twoway(200); // Permite el movimiento bidireccional con una velocidad de 200
  
 
  });
  </script>
  
  <style scoped>
  /* Puedes agregar estilos específicos para este componente aquí */
  </style>
  