<template>
  <div id="switcher">
    <p>switcher</p>
    <ul>
      <li v-for="item in datasources" :key="item">
        <button class="btn btn-primary" @click="$router.push('datasource')">Data<br>Source</button>
      </li>
      <li v-for="item in vizs" :key="item">
        <button class="btn btn-primary" @click="$router.push('viz')">Viz</button>
      </li>
    </ul>
  </div>
</template>

<script>

export default {
  name: 'Switcher',
  props: {
    datasources: Array,
    vizs: Array
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
