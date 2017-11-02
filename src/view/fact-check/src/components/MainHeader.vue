<template>
  <div class="container">
      <img id="logo" src="../assets/logo.png" alt="logo">
      <b-form-textarea id="textarea1"
                     v-model="text"
                     placeholder="Example: The president's securities are alien"
                     :rows="5"
                     :max-rows="10">
    </b-form-textarea>
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
    text-align: center;
    padding-top: 20px;
}
#logo{
  margin-bottom: 20px;
}
</style>
