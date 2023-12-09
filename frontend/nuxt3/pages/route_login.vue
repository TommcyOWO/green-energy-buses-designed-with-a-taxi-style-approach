<template>
  <div class="flex jc:center ai:center fixed top:50% left:50% translate(-50%,-50%) h:250px w:400px b:2|solid rbr:30">
  <div>
    <h2>您尚未登入或註冊</h2>
    <h4>You are not logged in or registered yet.</h4>
    <button @click="moveTo('account-login')" class="btn mt:20px cursor:pointer">登入/註冊</button>
  </div>
  </div>
</template>

<script setup lang="ts">
const router = useRouter();
const moveTo = (path: string) => router.push({ name: path });
</script>

<style scoped>

</style>