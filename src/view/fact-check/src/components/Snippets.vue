<template>
    <div>
        <div class="app container">
            <h5 class="title">"{{ title }}" - {{ matches }} resultados</h5>
            <ul>
              <li v-for="snippet in snippets"
                  v-bind:key="snippet._id">
                <div :id="'snippet-' + snippet._id" 
                    class="snippet"
                    v-bind:class="{correct: snippet.correct, incorrect: snippet.incorrect}">
                  <h5><strong> {{ snippet.title }} </strong></h5>
                <p> {{ snippet.text }}</p>
                </div>
                <div :id="'reference' + snippet._id" 
                      class="reference"
                      v-bind:class="{correct: snippet.correct, incorrect: snippet.incorrect}">
                  <span>Fonte: </span>
                  <a v-bind:href="snippet.url">{{ snippet.url | truncate(50) }}</a>
                </div>
                <div :id="'vote-' + snippet._id" class="vote-container" :ref="'vote-'+ snippet._id">
                    <img v-bind:id="'correct-'+ snippet._id" 
                          class="like" 
                          src="../assets/check.svg" 
                          alt="like"
                          @click="factTrue (snippet._id)">
                    <img v-bind:id="'incorrect-'+ snippet._id" 
                          class="deslike" 
                          src="../assets/uncheck.svg" 
                          alt="like"
                          @click="factFalse (snippet._id)">
                </div>
              </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
  methods: {
    factTrue: function (id) {
      this.snippets.forEach(function (element) {
        if (element._id === id) {
          if (element.correct) {
            element.correct = false
          } else {
            if (element.incorrect) {
              element.incorrect = false
            }
            element.correct = true
          }
        }
      })
    },
    factFalse: function (id) {
      this.snippets.forEach(function (element) {
        if (element._id === id) {
          if (element.incorrect) {
            element.incorrect = false
          } else {
            if (element.correct) {
              element.correct = false
            }
            element.incorrect = true
          }
        }
      })
    }
  },
  props: [
    'title',
    'snippets',
    'matches'
  ],
  filters: {
    truncate: function (string, value) {
      if (string.length > value) {
        return string.substring(0, value) + '...'
      }
      return string
    }
  }
}
</script>

<style scoped>
.correct{
  background-color: #DCEDC8;
}

.incorrect{
  background-color: #FFCDD2;
}

.container{
  margin-top: 30px;
  border-radius: 15px;
  border: solid 2px #EEEEEE;
  padding: 0;
}

.title{
  background-color: #EEEEEE;
  border-radius: 10px 10px 0 0;
  margin: 0;
  padding: 10px;
}

.snippet{
  border-top: solid 2px #EEEEEE;
  text-align: left;
  padding: 10px;
  margin: 0;
}

.reference{
  margin: 0;
  margin-bottom: 15px;
  padding: 5px;
}

.vote-container{
  margin: 0;
  margin-bottom: 15px;
}

.like, .deslike{
  height: 40px;
  width: 40px;
  margin: 5px;
  margin-left: 25px;
  margin-right: 25px;
}

.like, .deslike:hover{
  cursor: pointer;
}

ul{
  list-style: none;
  padding: 0;
  margin: 0;
}

</style>
