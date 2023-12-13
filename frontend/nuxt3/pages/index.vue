<template>
  <div class="abs top:100px left:50% translate(-50%,50%)">
    <nav>
      <span class="block">
        <h3>出發地</h3>
        <h4>Origin</h4>
        <input class="acinpu" type="text">
      </span>
      <span class="block my:20px">
        <h3>目的地</h3>
        <h4>Destination</h4>
        <input class="acinpu" type="text">
      </span>
    </nav>
    <section>
      <button class="btn blcok">叫車</button>
    </section>
</div>
</template>

<script setup lang="ts">
import Cookies from "cookies-ts";

const cookies = new Cookies();
const router = useRouter();
onMounted(()=>{
  const authKey = cookies.get("auth_key") || router.push({ name: "route_login" })
})
</script>

<style scoped>

</style>