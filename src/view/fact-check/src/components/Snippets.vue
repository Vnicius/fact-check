<template>
    <div>
        <div class="app container">
            <h3 class="title"> {{ title }}</h3>
            <p class="snippet"> {{ text }}</p>
            <div class="reference">
              <span>Fonte: </span>
              <a v-bind:href="url">{{ url }}</a>
            </div>
            <div id="vote" class="vote-container">
                <img class="like" src="../assets/like.svg" alt="like">
                <img class="deslike" src="../assets/deslike.svg" alt="like">
            </div>
        </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      title: 'Titulo',
      text: 'Lorem ipsum',
      url: 'http://www.google.com'
    }
  }
}
</script>

<style scoped>
.container{
  margin-top: 30px;
}

.title{
  background-color: gray;
  border-radius: 15px 15px 0 0;
  margin-bottom: 0;
}

.snippet{
  text-align: left;
  padding: 10px;
  border: solid 2px gray;
  border-bottom: none;
  margin: 0;
}

.reference{
  margin: 0;
  border: solid 2px gray;
  border-top: none;
}

.vote-container{
  margin: 0;
  border: solid 2px gray;
  border-top: none;
  border-radius: 0 0 15px 15px;
}

.like, .deslike{
  height: 50px;
  width: 50px;
  margin: 10px;
  margin-left: 25px;
  margin-right: 25px;
}
</style>
