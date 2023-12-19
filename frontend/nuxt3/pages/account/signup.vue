<template>
    <div class="abs top:50% left:50% translate(-50%,-50%)">
      <div class="h:450px w:300px rbr:40 b:2.3|solid bg:white">
        <nav class="mt:20px m:40px">
          <span class="block pt:10px">
            <h2>使用者名稱</h2>
            <h4>User Name</h4>
            <input v-model="username" class="acinpu" type="text">
          </span>
          <span class="block my:10px">
            <h2>電子郵件</h2>
            <h4>E-Mail</h4>
            <input v-model="email" class="acinpu" type="email">
          </span>
          <span class="block my:10px">
            <h2>密碼</h2>
            <h4>Password</h4>
            <input v-model="password" class="acinpu" type="password">
          </span>
        </nav>
        <section class=" mx:40px">
          <button @click="moveTo('account-logon')" class="btn cursor:pointer">登入</button>
          <button @click="moveTo('account-password_forgot')" class="btn ml:30px cursor:pointer">忘記密碼?</button>
          <button @click="sign_up()" class="btn w:200px cursor:pointer mt:10px">註冊</button>
        </section>
      </div>
    </div>
</template>

<script setup lang="ts">
import axios from "axios";
import Cookies from 'cookies-ts';
import conf from "@/assets/conf";

const username = ref("")
const password = ref("")
const email = ref("")

const router = useRouter();
const moveTo = (path: string) => router.push({ name: path });
const cookies = new Cookies();


const sign_up = async () => {
  const data = {
    "username":username.value,
    "password":password.value,
    "email":email.value
  }
  try {
    const response = await axios.post(conf.urls+"sign_up",data)
    moveTo("account-logon")
  } catch (error) {
    console.error(error);
  }
}

onMounted(() => {
  const authKey = cookies.get("auth_key")
  if (authKey !== null) {
    moveTo("index")
  }
})
</script>

<style scoped>

</style>