<template>
  <div>

  </div>
</template>

<script setup lang="ts">
import Cookies from "cookies-ts";

//setup
const cookies = new Cookies();
const router = useRouter();

//掛載完後檢查token
onMounted(() => {
  const authKey = cookies.get("auth_key") || router.push({ name: "route_login" })
})
</script>

<style scoped>

</style>