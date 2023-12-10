<template>
  <div class="abs top:50% left:50% translate(-50%,-50%)">
    <div class="h:450px w:300px rbr:40 b:2.3|solid bg:white">
      <nav class="mt:20px m:40px">
        <span class="block pt:50px">
          <h2>使用者名稱</h2>
          <h4>User Name</h4>
          <input v-model="username" class="acinpu" type="text">
        </span>
        <span class="block my:10px">
          <h2>密碼</h2>
          <h4>Password</h4>
          <input v-model="password" class="acinpu" type="password">
        </span>
      </nav>
      <section class="m:40px">
        <button @click="moveTo('account-signup')" class="btn cursor:pointer">註冊</button>
        <button @click="moveTo('account-password_forgot')" class="btn ml:30px cursor:pointer">忘記密碼?</button>
        <button @click="logon()" class="btn w:200px cursor:pointer mt:10px">登入</button>
      </section>
    </div>
  </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import conf from "@/assets/conf"

const router = useRouter();
const moveTo = (path: string) => router.push({ name: path });

const username = ref("")
const password = ref("")

const logon = async () => {
  const data = new URLSearchParams();
  data.append('username', username.value);
  data.append('password', password.value);

  const config = {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  };
  try {
    const response = await axios.post(conf.urls + 'logon', data, config);
    const token = response.data.access_token;
    console.log(token)
  } catch (error:any) {
    console.error(error.response)
  }
}
</script>

<style scoped>

</style>