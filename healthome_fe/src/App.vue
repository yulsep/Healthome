<template>
  <div>
    <router-view v-on:completedLogIn="completedLogin" v-on:completedSignUp="completedSignup">
    </router-view>
  </div>
</template>

<script>
export default {
  name: 'App',

  data: function () {
    return {
      is_auth: false
    }
  },

  components: {

  },

  methods: {
    verifyAuth: function () {
      if (this.is_auth == false)
        this.$router.push({ name: "Login" })
    },
    loadLogIn: function () {
      this.$router.push({ name: "Login" })
    },
    loadSignUp: function () {
      this.$router.push({ name: "Signup" })
    },
    completedLogIn: function (data) { },
    completedSignUp: function (data) { },
  },

  created: function () {
    this.verifyAuth()
  }

}
</script>

<style>
body {
  margin: 0;
  padding: 0;
}
</style>