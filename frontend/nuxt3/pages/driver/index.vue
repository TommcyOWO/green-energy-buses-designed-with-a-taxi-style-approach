<template>
  <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
    <section class="text:center">
      <nav>
        <span class="p:20px" v-for="item in passengers" :key="item._id[0]">
          <p>起始點: {{ item.origins }}</p>
          <p>目的地: {{ item.destination }}</p>
          <p>乘客: {{ item.users.join(', ') }}</p>
        </span>
      </nav>
      <div>
        <div v-if="passengers">
          <button @click="confirmAction" class="btn m:10px cursor:pointer">確定</button>
          <button @click="router.go(0)" class="btn m:10px cursor:pointer">取消</button>
        </div>
        <button v-else @click="get_passenger" class="btn cursor:pointer m:10px">搜尋乘客</button>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import Cookies from 'cookies-ts';
import axios from 'axios';
import conf from '@/assets/conf'
import { useLocalStorage } from '@vueuse/core';

const cookies = new Cookies();
const router = useRouter();
const authkey = ref("");
const passengers = ref();

const get_passenger = async () => {
  const headers = {
    'Authorization': `Bearer ${authkey.value}`
  };

  try {
    const response = await axios.get(conf.urls + 'get_passenger', {
      headers
    });
    passengers.value = JSON.parse(response.data);
  } catch (error) {
    console.error(error);
  }
};

const confirmAction =async () => {
  const passengersData = useLocalStorage('passengersData', JSON.stringify(passengers.value));
  console.log(passengersData.value)
}

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
