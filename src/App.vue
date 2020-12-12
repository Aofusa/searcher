<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <router-view></router-view>
    <Generator @add-datasource="datasources.push(1)" @add-viz="vizs.push(1)"/>
    <Switcher :datasources=this.datasources :vizs=this.vizs />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Switcher from './components/Switcher.vue'
import Generator from './components/Generator.vue'
// import DataSource from './components/DataSource.vue'
// import Viz from './components/Viz.vue'

export default {
  name: 'App',
  data () {
    return {
      datasources: [1,2],
      vizs: [3]
    }
  },
  components: {
    HelloWorld,
    Switcher,
    Generator,
    // DataSource,
    // Viz
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
