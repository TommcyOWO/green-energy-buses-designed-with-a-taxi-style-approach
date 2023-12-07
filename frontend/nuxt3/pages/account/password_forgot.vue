<template>
    <div class="abs top:50% left:50% translate(-50%,-50%)">
      <div class="h:450px w:300px rbr:40 b:2.3|solid">
        <nav class="mt:50px m:40px">
          <span class="block pt:50px">
            <h2>使用者名稱</h2>
            <h4>User Name</h4>
            <input class="acinpu" type="text">
          </span>
          <span class="block my:10px">
            <h2>密碼</h2>
            <h4>Password</h4>
            <input class="acinpu" type="password">
          </span>
        </nav>
        <section class="mt:60px mx:40px">
          <button @click="moveTo('account-login')" class="btn mx:15px cursor:pointer">登入</button>
          <button @click="moveTo('account-signup')" class="btn mx:15px cursor:pointer">註冊</button>
        </section>
      </div>
    </div>
</template>

<script setup lang="ts">
const router = useRouter();
const moveTo = (path: string) => router.push({ name: path });
</script>

<style scoped>

</style>