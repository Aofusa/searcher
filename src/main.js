import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import { BootstrapVue } from './plugins/bootstrap-vue'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')


Vue.use(BootstrapVue)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
