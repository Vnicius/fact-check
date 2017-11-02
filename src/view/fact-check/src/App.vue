<template>
  <div class="app">
    <MainHeader/>
    <Snippets/>
    <Snippets/>
  </div>
</template>

<script>
import MainHeader from './components/MainHeader.vue'
import Snippets from './components/Snippets.vue'
export default{
  name: 'FactCheck',
  components: {
    MainHeader,
    Snippets
  }
}
</script>

<style>
.app{
  text-align: center;
}
</style>
