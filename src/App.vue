<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <Switcher />
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Switcher from './components/Switcher.vue'
// import DataSource from './components/DataSource.vue'
// import Viz from './components/Viz.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    Switcher,
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
