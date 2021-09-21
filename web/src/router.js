import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)


export default new Router({
 mode: 'history',
 base: process.env.BASE_URL,
 routes:[
   {
      path:'/',
      name:'home',
      component: () => import('./views/Home.vue')
   },
   {
      path:'/folders',
      name:'folder_index',
      component: () => import('./views/Folder/index.vue')
   },
   
   {
      path:'/folder_show/:id/tasks',
      name:'task_index',
      component: () => import('./views/Task/index.vue')
   },
   {
      path:'/folder_new',
      name:'folder_new',
      component: () => import('./views/Folder/new.vue')
   },
   {
      path:'/folder_show/:id',
      name:'folder_show',
      component: () => import('./views/Folder/show.vue')
   }, 
 ]
})
