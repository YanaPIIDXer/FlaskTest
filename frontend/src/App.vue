<template>
  <div id="app">
    <form @submit="onSubmit">
      <input type="text" v-model="message" />
      <input type="submit" value="送信" />
    </form>
    <button @click="fetchMessage">メッセージ取得</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  data: function () {
    return {
      message: "Hello, World",
    }
  },
  methods: {
    /**
     * 送信
     */
    onSubmit: async function (e) {
      e.preventDefault()

      try {
        const response = await axios.post("http://localhost:3000/message", {
          message: this.message,
        })
        if (!response || !response.data.result) { throw response }
      } catch (error) {
        console.error(error)
        alert("エラー")
        return
      }

      alert("送信しました") 
      this.message = ""
    },
    /**
     * メッセージ取得
     */
    fetchMessage: async function () {
      let msg = ""
      try {
        const response = await axios.get("http://localhost:3000")
        if (!response) { throw response }
        msg = response.data.message
      } catch (error) {
        console.error(error)
        alert("エラー")
        return
      }
      alert(msg)
    }
  },
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
