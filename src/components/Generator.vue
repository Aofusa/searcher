<template>
  <div id="generator">
    <p>Generator</p>
    <button class="btn btn-primary" @click="$emit('add-datasource')">Add<br>Data<br>Source</button>
    <button class="btn btn-primary" @click="$emit('add-viz')">Add<br>Viz</button>
  </div>
</template>

<script>

export default {
  name: 'Generator',
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
