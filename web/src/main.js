import Vue from 'vue';
import App from './App.vue';
import router from './router'; 

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue';
import VueFlashMessage from 'vue-flash-message';


Vue.use(BootstrapVue);
Vue.use(IconsPlugin);
Vue.use(VueFlashMessage);

new Vue({
  router, // router added to the Vue instance
  render: function(h) {
    return h(App);
  },
}).$mount('#app');
