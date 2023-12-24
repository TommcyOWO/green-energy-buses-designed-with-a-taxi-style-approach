<template>
  <div>

  </div>
</template>

<script setup lang="ts">
import Cookies from "cookies-ts";

//setup
const cookies = new Cookies();
const router = useRouter();

const authkey = ref("");

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

<style scoped>

</style>