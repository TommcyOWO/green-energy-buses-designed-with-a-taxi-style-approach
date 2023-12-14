<template>
    <div class="abs top:50% left:50% translate(-50%,-50%)">
      <div class="h:500px w:300px rbr:40 b:2.3|solid bg:white">
        <nav class="mt:20px mx:40px">
          <span class="block">
            <h2>使用者名稱</h2>
            <h4>User Name</h4>
            <input v-model="username" class="acinpu" type="text">
          </span>
          <span class="block my:5px">
            <h2>電子郵件</h2>
            <h4>E-Mail</h4>
            <input v-model="email" class="acinpu" type="email">
          </span>
          <span class="block my:5px">
            <h2>新密碼</h2>
            <h4>New Password</h4>
            <input v-model="n_password" class="acinpu" type="password">
          </span>
          <span class="block mt:5px">
            <h2>確認密碼</h2>
            <h4>Verify Password</h4>
            <input v-model="v_password" class="acinpu" type="password">
          </span>
        </nav>
        <section class="mt:20px mx:40px">
          <button @click="moveTo('account-logon')" class="btn cursor:pointer">登入</button>
          <button @click="moveTo('account-signup')" class="btn ml:65px cursor:pointer">註冊</button>
          <button @click="reset()" class="btn w:200px cursor:pointer mt:10px">重製</button>
        </section>
      </div>
    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import conf from "@/assets/conf"
import Cookies from 'cookies-ts';

const router = useRouter();
const moveTo = (path: string) => router.push({ name: path });

const username = ref("")
const email = ref("")
const n_password = ref("")
const v_password = ref("")
const cookies = new Cookies();

const reset = async () => {
  try {
    if (n_password.value !== v_password.value) {
      console.log("no match");
      return "Passwords do not match";
    }

    const data = {
      "username": username.value,
      "password": n_password.value,
      "email": email.value
    };

    const response = await axios.post(conf.urls + "reset", data);
    if(response.data.message === "Reset done"){
      moveTo("account-login")
    }
  } catch (error) {
    console.error("Request failed:", error);
  }
};

onMounted(() => {
  const authKey = cookies.get("auth_key")
  if (authKey !== null) {
    moveTo("index")
  }
})
</script>

<style scoped>

</style>