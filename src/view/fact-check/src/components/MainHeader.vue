<template>
  <div class="container">
      <img id="logo" src="../assets/logo.png" alt="logo">
      <b-form-textarea id="textarea1"
                     v-model="text"
                     placeholder="Exemplo: Foram construídas 25 escolas em 2016"
                     :rows="5"
                     :max-rows="10">
    </b-form-textarea>
    <b-button class="btn-send" variant="outline-success">
        Enviar
    </b-button>
  </div>
</template>

<script>
export default{
  data () {
    return {
      text: ''
    }
  }
}
</script>

<style scoped>
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
</style>
