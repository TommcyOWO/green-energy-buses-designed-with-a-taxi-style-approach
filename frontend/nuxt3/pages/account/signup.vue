<template>
    <div class="abs top:50% left:50% translate(-50%,-50%)">
      <div class="w:300px mt:150px rbr:40 b:2.3|solid bg:white">
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
          <span class="block my:10px">
              <h2>身分</h2>
              <h4>Identity</h4>
              <select class="tselect" v-model="identity">
                <option :value="false">乘客|Passenger</option>
                <option :value="true">司機|Driver</option>
              </select>
          </span>
        </nav>
        <section class=" mx:40px mb:20px">
          <button @click="moveTo('account-login')" class="btn cursor:pointer">登入</button>
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

//setup
const username = ref("")
const password = ref("")
const email = ref("")
const identity = ref(false)

//setup router
const router = useRouter();
const moveTo = (path: string) => router.push({ name: path });
const cookies = new Cookies();

//func of sign up
const sign_up = async () => {
  const data = {
    "driver":identity.value,
    "username":username.value,
    "password":password.value,
    "email":email.value
  }
  try {
    const response = await axios.post(conf.urls+"sign_up",data)
    moveTo("account-login")
  } catch (error) {
    console.error(error);
  }
}

//掛載後確認是否已登入
onMounted(() => {
  const authKey = cookies.get("auth_key")
  if (authKey !== null) {
    moveTo("index")
  }
})
</script>

<style scoped>

</style>