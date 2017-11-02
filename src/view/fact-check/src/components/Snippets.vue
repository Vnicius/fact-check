<template>
    <div>
        <div class="app container">
            <h3 class="title"> {{ title }}</h3>
            <ul>
              <li v-for="snippet in snippets"
                  v-bind:key="snippet.key">
                <p class="snippet"> {{ snippet.text }}</p>
                <div class="reference">
                  <span>Fonte: </span>
                  <a v-bind:href="snippet.url">{{ snippet.url }}</a>
                </div>
                <div id="vote" class="vote-container">
                    <img class="like" src="../assets/like.svg" alt="like">
                    <img class="deslike" src="../assets/deslike.svg" alt="like">
                </div>
              </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
  props: [
    'title',
    'snippets'
  ]
}
</script>

<style scoped>
.container{
  margin-top: 30px;
  border-radius: 15px;
  border: solid 2px gray;
  padding: 0;
}

.title{
  background-color: gray;
  border-radius: 10px 10px 0 0;
  margin: 0;
}

.snippet{
  border-top: solid 2px gray;
  text-align: left;
  padding: 10px
}

.reference{
  margin: 0;
  margin-bottom: 15px;
}

.vote-container{
  margin: 0;
  margin-bottom: 15px;
}

.like, .deslike{
  height: 50px;
  width: 50px;
  margin: 10px;
  margin-left: 25px;
  margin-right: 25px;
}

ul{
  list-style: none;
  padding: 0;
  margin: 0;
}
</style>
