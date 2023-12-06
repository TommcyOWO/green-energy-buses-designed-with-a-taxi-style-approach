<template>
  <div class="flex fixed w:100% h:30px m:10px ai:center">
    <IconMenu2 @click="menu_toggle()" class="flex hide@>md"/>
      <ul :class="{ 'hidden@<md': m_value }" class="{rel;top:55px;right:24px}@<md list-style:none flex@>md f:20px">
        <li class="cursor:pointer mx:10px f:semibold f:20px" @click="moveTo('index')">叫車服務</li>
        <li class="cursor:pointer mx:10px f:semibold f:20px" @click="moveTo('bus_information')">公車資訊</li>
        <li class="cursor:pointer mx:10px f:semibold f:20px" @click="moveTo('bus_stops')">公車站點</li>
      </ul>
  </div>
  <slot/>
</template>

<script setup lang="ts">
import {IconMenu2} from "@tabler/icons-vue";
import "@master/css";

const router = useRouter();
const moveTo = (path: string) => router.push({ name: path });
const [m_value, menu_toggle] = useToggle(true);
</script>

<style scoped>

</style>