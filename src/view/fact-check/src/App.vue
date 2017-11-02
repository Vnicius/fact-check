<template>
  <div class="app">
    <div class="container">
      <img id="logo" src="./assets/logo.png" alt="logo">
      <b-form-textarea id="textarea-claim"
                     v-model="claim"
                     placeholder="Exemplo: Foram construídas 25 escolas em 2016"
                     :rows="5"
                     :max-rows="10">
      </b-form-textarea>
      <b-button class="btn-send" 
                variant="outline-success"
                @click="getSnippets">
          Pesquisar
      </b-button>
    </div>
    <img v-if="wait" 
        src="./assets/loading.gif" 
        alt=""
        class="loading">
    <Snippets v-for="snip in snippets"
              v-bind:key="snip.id"
              v-bind:title="snip.title"
              v-bind:snippets="snip.snippets"/>
    <div v-if="full" class="container">
      <b-button class="btn-send" 
          variant="outline-success"
          @click="send">
          Enviar
      </b-button>
    </div>          
    
  </div>
</template>

<script>
import Snippets from './components/Snippets.vue'
export default{
  name: 'FactCheck',
  components: {
    Snippets
  },
  data () {
    return {
      snippets: [],
      claim: '',
      wait: false,
      full: false
    }
  },
  methods: {
    getSnippets: function () {
      if (this.claim !== '') {
        this.snippets = []
        this.full = false
        this.wait = true
        this.$http.post('http://localhost:5000/snippets', {text: this.claim}).then((response) => {
          this.snippets = JSON.parse(response.bodyText)
          this.wait = false
          this.full = true
        })
      }
    },
    send: function () {
      this.$http.post('http://localhost:5000/send', this.snippets).then((response) => {
        if (response.bodyText) {
          alert('Enviado!')
        }
      })
      console.log(JSON.parse(JSON.stringify(this.snippets)))
    }
  }
}
</script>

<style>
.app{
  text-align: center;
  padding: 20px;
}
.container{
  text-align: center
}
#logo{
  margin-bottom: 20px;
}

.btn-send{
  margin-top: 30px;
  width: 100%;
}

.btn-send:hover{
  cursor: pointer;
}

.form-control:focus {
  border-color: #A5D6A7;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 8px rgba(0, 255, 0, 0.6);
}

.loading{
  margin-top: 50px;
  height: 50px;
  width: 50px;
}
</style>
