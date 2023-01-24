import { createRouter, createWebHistory } from 'vue-router'
//import App from './App.vue'

const routes = [{
  path: '/',
  name: 'root',
  component: () => import('./App')
},
{
  path:'/login',
  name:"Login",
  component:() => import('./views/auth/Login')
},
{
  path:'/signup',
  name:"Signup",
  component:() => import('./views/auth/Signup')
}
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;