<template>
  <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);">
    <section v-if="!confirms_data" class="text:center">
      <nav>
        <span class="p:20px" v-for="item in passengers" :key="item.ids[0]">
          <p>起始點: {{ item.origins }}</p>
          <p>目的地: {{ item.destination }}</p>
          <p>乘客: {{ item.users.join(', ') }}</p>
        </span>
      </nav>
      <div>
        <div v-if="passengers">
          <button @click="confirm" class="btn m:10px cursor:pointer">確定</button>
          <button @click="router.go(0)" class="btn m:10px cursor:pointer">取消</button>
        </div>
        <button v-else @click="get_passenger" class="btn cursor:pointer m:10px">搜尋乘客</button>
      </div>
    </section>
    <section v-else class="text:center">
        <nav>
        <span class="p:20px" v-for="item in passengers" :key="item.ids[0]">
          <p>起始點: {{ item.origins }}</p>
          <p>目的地: {{ item.destination }}</p>
          <p>乘客: {{ item.users.join(', ') }}</p>
        </span>
        </nav>
      <button @click="finish" class="btn cursor:pointer">結束</button>
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
const confirms_data = ref()
let passengers_data: any

const get_passenger = async () => {
  const headers = {
    'Authorization': `Bearer ${authkey.value}`,
    'Content-Type': 'application/json'
  };
  try {
    const response = await axios.get(conf.urls + 'get_passenger', {headers});
    passengers_data = passengers.value = JSON.parse(response.data);
    console.log(JSON.parse(response.data))
  } catch (error) {
    console.error(error);
  }
};

const confirm =async () => {
  const headers = {
    'Authorization': `Bearer ${authkey.value}`,
    'Content-Type': 'application/json'
  };
  const datas = {
    data: passengers_data
  }
  try {
    const responses = await axios.post(conf.urls+"confirm",datas,{headers})
    confirms_data.value = responses.data
  } catch (error) {
    console.error(error)
  }
}

const finish = async () => {
  try {
    const response = await axios.post(
      conf.urls + "finish",
      null,
      {
        headers: {
          'Authorization': `Bearer ${authkey.value}`
        }
      }
    );

    passengers.value = confirms_data.value = passengers_data = null;
    router.go(0);
  } catch (error:any) {
    if (error.response && error.response.status === 401) {
      console.error('未授權錯誤:', error.response.data);
    } else {
      console.error('請求錯誤:', error.message);
    }
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
