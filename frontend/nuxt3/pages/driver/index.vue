<template>
  <div class="abs top:50% left:50% translate(-50%,-50%)">
    <section>
      <div>
        
      </div>
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

const get_passenger = async () => {
  const headers = {
    'Authorization': `Bearer ${authkey.value}`,
    'Content-Type': 'application/json',
  };

  try {
    const response = await axios.get(conf.urls + 'get_passenger', {
      headers,
      withCredentials: true,
    });

    console.log(response);
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
