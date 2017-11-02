<template>
  <div class="app">
    <MainHeader/>
    <Snippets v-for="snip in snippets"
              v-bind:key="snip.id"
              v-bind:title="snip.title"
              v-bind:snippets="snip.snippets"/>
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
  },
  data () {
    return {
      snippets: [
        {
          id: '1',
          title: 'Título 1',
          snippets: [
            {
              key: '33',
              text: 'Isso é o texto 22222',
              url: 'http://www.facebook.com.br'
            },
            {
              key: '33',
              text: 'Isso é o texto 111111',
              url: 'http://www.facebook.com.br'
            }
          ]
        }
      ]
    }
  }
}
</script>

<style>
.app{
  text-align: center;
}
</style>
