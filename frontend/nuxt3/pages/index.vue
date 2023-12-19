<template>
  <div class="abs top:100px left:50% translate(-50%,50%)
    b:2px|solid rbr:20">
    <nav class="mx:60px mt:60px">
      <span class="block">
        <h3>出發地</h3>
        <h4>Origin</h4>
        <select class="tselect">
          <option value="1">站點1</option>
          <option value="2">站點2</option>
          <option value="3">站點3</option>
          <option value="4">站點4</option>
        </select>
      </span>
      <span class="block my:10px">
        <h3>目的地</h3>
        <h4>Destination</h4>
        <select class="tselect">
          <option value="1">站點1</option>
          <option value="2">站點2</option>
          <option value="3">站點3</option>
          <option value="4">站點4</option>
        </select>
      </span>
    </nav>
    <section class="flex jc:center ai:center my:20px">
      <button class="btn blcok cursor:pointer">叫車</button>
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
