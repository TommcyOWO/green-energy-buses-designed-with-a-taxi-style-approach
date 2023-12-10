<template>
  <div>

  </div>
</template>

<script setup lang="ts">
import Cookies from "cookies-ts";

const cookies = new Cookies();
const router = useRouter();

onMounted(() => {
  const authKey = cookies.get("auth_key") || router.push({ name: "route_login" })
})
</script>

<style scoped>

</style>