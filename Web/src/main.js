import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'


const app = createApp(App)

app.use(router)

app.mount('#app')
console.log(import.meta.env) // 123
console.log(import.meta.env.VITE_SOME_KEY) // 123
