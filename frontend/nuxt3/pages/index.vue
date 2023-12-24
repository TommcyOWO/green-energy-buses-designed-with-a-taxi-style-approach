<template>
  <div class="abs top:50% left:50% translate(-50%,-50%)
    b:2px|solid rbr:20">
    <nav class="mx:60px mt:60px">
      <span class="block">
        <h3>出發地</h3>
        <h4>Origin</h4>
        <select v-model="origin_" class="tselect">
          <option value="1">站點1</option>
          <option value="2">站點2</option>
          <option value="3">站點3</option>
          <option value="4">站點4</option>
        </select>
      </span>
      <span class="block my:10px">
        <h3>目的地</h3>
        <h4>Destination</h4>
        <select v-model="destination_" class="tselect">
          <option value="1">站點1</option>
          <option value="2">站點2</option>
          <option value="3">站點3</option>
          <option value="4">站點4</option>
        </select>
      </span>
    </nav>
    <section class="flex jc:center ai:center my:20px">
      <button @click="call" :class="{ 'cursor:not-allowed': clicked, 'cursor:pointer': !clicked }" class="btn blcok">叫車</button>
    </section>
</div>
</template>

<script setup lang="ts">
import Cookies from "cookies-ts"
import axios from "axios";
import conf from  "@/assets/conf"

//setup
const cookies = new Cookies();
const router = useRouter();

const origin_ = ref('1')
const destination_ = ref('1')
const authkey = ref("");
const clicked = ref(false)

const call = async () => {
  const data = {
    origin: origin_.value,
    destination: destination_.value
  };
  const headers = {
    'Authorization': `Bearer ${authkey.value}`,
    'Content-Type': 'application/json'
  };
  try {
    const response = await axios.post(conf.urls + "call", data,{headers});
  } catch (error) {
    clicked.value = true
  }
};

// 掛載完後檢查 token
onMounted(async () => {
  const token = cookies.get("auth_key");
  if (token) {
    authkey.value = token;
  } else {
    await router.push({ name: "route_login" });
  }
});

</script>
