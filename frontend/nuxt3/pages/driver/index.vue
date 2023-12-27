<template>
  <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
    <section>
      <ul>
        <li v-for="item in passengers" :key="item._id[0]">
          <p>起始點: {{ item.origins }}</p>
          <p>目的地: {{ item.destination }}</p>
          <p>使用者: {{ item.users.join(', ') }}</p>
        </li>
      </ul>
      <button @click="get_passenger" class="btn cursor:pointer">搜尋乘客</button>
    </section>
  </div>
</template>

<script setup lang="ts">
import Cookies from 'cookies-ts';
import axios from 'axios';
import conf from '@/assets/conf'

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
