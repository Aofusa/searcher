import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import VueRouter from 'vue-router'
import { BootstrapVue } from './plugins/bootstrap-vue'
import App from './App.vue'
import DataSource from './components/DataSource.vue'
import Viz from './components/Viz.vue'

Vue.config.productionTip = false

Vue.use(VueRouter)

const routes = [
  { path: '/datasource', component: DataSource },
  { path: '/viz', component: Viz }
]

const router = new VueRouter({
  routes: routes
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
Vue.use(BootstrapVue)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

